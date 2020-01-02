#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Will Mathewson, Nathan Ward'
PROFILE_IMAGE = 'IMG_0825.png'
BIO = "A post-modern identity crisis with Will & Nathan"
SITENAME = 'Cabbage and Shame'
SITEURL = ''
THEME = 'theme'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
GITHUB_URL = 'https://github.com/neanias/cabbageandshame'

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
SIDEBAR_LINKS = (('Categories', '/categories'),
                 ('Tags', '/tags'),
                 ('Authors', '/authors'),
                 )

# Social widget
SOCIAL = (('github', 'https://github.com/neanias/cabbageandshame'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
