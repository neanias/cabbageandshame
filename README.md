# Cabbage & Shame

This is the source for the [Cabbage & Shame website](https://www.cabbageandshame.co.uk).

## Requirements

To build this project, you will need to install:

* [Python 3.8+](https://www.python.org/downloads/)
* [Pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)
  - To install the dependencies, run `pipenv install --dev`

## Development

To serve the website locally, run

```console
$ pipenv run pelican --listen
```

To generate the website HTML pages from the articles & pages, run

```console
$ pipenv run pelican content
```

To create a new template article, run

```console
$ pipenv run invoke generate-article -t "My awesome title here"
Your template article can be found here: content/2020/1/my_awesome_title_here.md
```

This will create a new article with the title and date fields populated as well as category and tags
fields filled with placeholders.

## Publishing

To publish this project, run:

```
$ pipenv run invoke gh-pages
```
