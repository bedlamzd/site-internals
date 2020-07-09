#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)
sys.path.append(os.curdir + '/internals')

import custom_filters

AUTHOR = 'bedlamzd'
SITENAME = 'bedlamzd'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = [
    'img',
    'extra',
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

MAIN_PIC = 'main.jpg'
DEFAULT_THUMB = 'default_thumb.png'

ARTICLE_ORDER_BY = 'reversed-date'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%-d %B %Y'
DATE_FORMATS = {
    'ru': ('ru_RU', '%-d %B %Y'),
}

MENUITEMS = (
    # ('ГЛАВНАЯ', ''),
    # ('Подробнее', 'about.html'),
)

SLUGIFY_SOURCE = 'basename'

PLUGIN_PATHS = ['pelican_plugins', ]

PLUGINS = [
    'm.htmlsanity',
    'pelican_alias',
]

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'

THEME_STATIC_DIR = 'theme'
THEME = './theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

JINJA_FILTERS = {function: getattr(custom_filters, function) for function in dir(custom_filters) if
                 not function.startswith('_')}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_SAVE_AS = PAGE_SAVE_AS = '{path_no_ext}/index.html'
ARTICLE_URL = PAGE_URL = '{path_no_ext}/'

TELEGRAM_LINK = 'https://t.me/bedlamzd'
EMAIL_LINK = 'mailto:bedlamzd@gmail.com'
GITHUB_LINK = 'https://github.com/bedlamzd'

DIRECT_TEMPLATES = [
    'index',
    'categories',
    'tags',
]
