# -*- coding: utf-8 -*-

import datetime
import os
import shutil
import sys

from dateutil import tz
from invoke import task
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file
from pelican.utils import slugify

SETTINGS_FILE_BASE = "pelicanconf.py"
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    "settings_base": SETTINGS_FILE_BASE,
    "settings_publish": "publishconf.py",
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    "deploy_path": SETTINGS["OUTPUT_PATH"],
    # Github Pages configuration
    "github_pages_branch": "gh-pages",
    "commit_message": "'Publish site at {}'".format(
        datetime.datetime.now().isoformat()
    ),
    # Port for `serve`
    "port": 8000,
    # Slug regex substitution
    "slug_regex_substitutions": (
        DEFAULT_CONFIG["SLUG_REGEX_SUBSTITUTIONS"] + [(r"[-\s]+", "_")]
    ),
}


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task
def build(c):
    """Build local version of site"""
    c.run("pelican -s {settings_base}".format(**CONFIG))


@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run("pelican -d -s {settings_base}".format(**CONFIG))


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run("pelican -r -s {settings_base}".format(**CONFIG))


@task
def serve(c):
    """Serve site at http://localhost:$PORT/ (default port is 8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"], ("", CONFIG["port"]), ComplexHTTPRequestHandler
    )

    sys.stderr.write("Serving on port {port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task(pre=[clean])
def preview(c):
    """Cleans any compiled files then builds production version of site"""
    c.run("pelican -s {settings_publish}".format(**CONFIG))


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server

    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG["settings_base"], lambda: build(c))
    # Watch content source files
    content_file_extensions = [".md", ".rst"]
    for extension in content_file_extensions:
        content_blob = "{0}/**/*{1}".format(SETTINGS["PATH"], extension)
        server.watch(content_blob, lambda: build(c))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS["THEME"]
    server.watch("{}/templates/*.html".format(theme_path), lambda: build(c))
    static_file_extensions = [".css", ".js"]
    for extension in static_file_extensions:
        static_file = "{0}/static/**/*{1}".format(theme_path, extension)
        server.watch(static_file, lambda: build(c))
    # Serve output path on configured port
    server.serve(port=CONFIG["port"], root=CONFIG["deploy_path"])


@task
def publish(c):
    """Publish to production via rsync"""
    c.run("pelican -s {settings_publish}".format(**CONFIG))
    c.run(
        'rsync --delete --exclude ".DS_Store" -pthrvz -c '
        '-e "ssh -p {ssh_port}" '
        "{} {ssh_user}@{ssh_host}:{ssh_path}".format(
            CONFIG["deploy_path"].rstrip("/") + "/", **CONFIG
        )
    )


@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    preview(c)
    c.run(
        "ghp-import -b {github_pages_branch} "
        "-m {commit_message} "
        "{deploy_path} -p".format(**CONFIG)
    )


@task(help={"title": 'The title for the new article. Defaults to "Article title".'})
def generate_article(c, title="Article title"):
    """Generates a new empty article for the blog.

    The current date will be used for the metadata as well as the positioning
    of the article in the `content` tree.
    """
    current_datetime = datetime.datetime.now(tz=tz.gettz())

    # Create a slug for the file system using Pelican's slugification code
    slug = slugify(title, regex_subs=CONFIG["slug_regex_substitutions"])

    year_and_month_path = os.path.join(
        "content", str(current_datetime.year), str(current_datetime.month)
    )
    os.makedirs(year_and_month_path, exist_ok=True)

    full_path = os.path.join(year_and_month_path, f"{slug}.md")

    if os.path.exists(full_path):
        sys.exit(
            f"Error: {full_path} already exists! Please use a different "
            "title for your post."
        )

    with open(full_path, "w") as f:
        metadata = {
            "Title": title,
            "Date": current_datetime.isoformat(timespec="seconds"),
            "Category": "TODO: CATEGORISE",
            "Tags": "TODO: TAG",
            "Author": "Some Person",
            "Summary": "Short summary about the article",
        }

        for key, value in metadata.items():
            f.write(f"{key}: {value}\n")

        f.write(
            "\nAdd some content here. Here's a cheat sheet on markdown: "
            "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"
        )

        f.write("\n")

    print(f"Your template article can be found here: {full_path}")
