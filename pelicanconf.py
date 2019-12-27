#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Will Mathewson, Nathan Ward'
SITENAME = 'cabbageandshame'
SITEURL = f'www.{SITENAME}.co.uk'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_METADATA = {
    'status': 'draft',
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.smarty': {},
    },
}

# Blogroll
LINKS = (('Source', 'https://github.com/neanias/cabbageandshame'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
