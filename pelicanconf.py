#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vincent Chov'
SITENAME = 'Vincent Chov'
SITETITLE = 'Vincent Chov'
SITESUBTITLE = 'Graduating CSE major at UConn Storrs'
SITEDESCRIPTION = 'Vincent Chov\'s personal website'
SITEURL = ''
PATH = 'content'
SITELOGO = '/images/vincent_chov.jpg'

STATIC_PATHS = ['images', 'docs', 'extra/CNAME', 'static']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},'extra/custom.css': {'path': 'static/custom.css'},}
CUSTOM_CSS = 'static/custom.css'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Theme
THEME = 'themes/Flex'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Resume', '{filename}/docs/VincentChovResume.pdf'),)

# Social widget
SOCIAL = (('github', 'https://github.com/vincentchov'),
          ('linkedin', 'https://linkedin.com/in/vincentchov'),)

DEFAULT_PAGINATION = 10

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2017

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Enable pelican-alias
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican_alias', 'sitemap']

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
