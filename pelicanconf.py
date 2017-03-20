#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vincent Chov'
SITENAME = 'Vincent Chov'
SITETITLE = 'Vincent Chov'
SITESUBTITLE = 'Graduating CSE major at UConn Storrs'
SITEDESCRIPTION = 'Vincent Chov\'s personal website'
SITEURL = 'http://localhost:8000'
SITELOGO = '/images/vincent_chov.jpg'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Theme
THEME = '/home/vincenzo/pelican-themes/Flex'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About Me', 'http://getpelican.com/'),
         ('Resume', 'http://python.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2017

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
