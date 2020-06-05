#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from pymdownx import emoji

AUTHOR = "Will Mathewson, Nathan Ward"
PROFILE_IMAGE = "IMG_0825.png"
BIO = "A post-modern identity crisis with Will & Nathan"
SITENAME = "Cabbage and Shame"
SIDEBAR_NAME = "Cabbage & Shame"
SITEURL = ""
THEME = "theme"

PATH = "content"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"
GITHUB_URL = "https://github.com/neanias/cabbageandshame"

ARTICLE_URL = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME",},
}

DEFAULT_METADATA = {
    "status": "draft",
}

MARKDOWN = {
    "extensions": ["pymdownx.emoji", "pymdownx.tilde",],
    "extension_configs": {
        "markdown.extensions.smarty": {},
        "pymdownx.emoji": {
            "emoji_index": emoji.twemoji,
            "emoji_generator": emoji.to_svg,
        },
    },
}

# Blogroll
SIDEBAR_LINKS = (
    ("Categories", "/categories"),
    ("Tags", "/tags"),
    ("Authors", "/authors"),
)

# Social widget
SOCIAL = (("github", "https://github.com/neanias/cabbageandshame"),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
