#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('.')

AUTHOR = u'Bartosz Plotka'
SITENAME = u'Moody Paths'
SITEURL = ''

import filters
JINJA_FILTERS = { 'sidebar': filters.sidebar,
                  'extract_trans': filters.extract_trans }

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

MENUITEMS = (
    ('HOME', '/'),
    ('ABOUT', '/pages/about.html'),
)

DEFAULT_PAGINATION = 3
POST_LIMIT = 3

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')
DISPLAY_CATEGORIES_ON_MENU = True

# Formatting for urls
# ARTICLE_DIR = 'blog'
ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

ARCHIVES_URL = "blog"
ARCHIVES_SAVE_AS = "blog/index.html"

PAGE_PATHS = ['pages']
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

USE_FOLDER_AS_CATEGORY = True

DEFAULT_LANG = "en"

SHOW_TAGS = False

THEME = "../twenty-pelican-html5up"

PLUGIN_PATHS = ["../plugins", "../plugins/pelican-plugins"]
PLUGINS = ["image_process", "i18n_subsites", "better_figures_and_images"]

PICK_A_MONTH = 'Pick a month'

I18N_SUBSITES = {
    'en': {
      'CATEGORY_TITLE': 'What happened this month?',
      'POSTED_IN': 'Posted in',
      'POSTED_ON': 'Posted on',
      'CREATED_WHERE': 'Country: ',
      'ABOUT' : 'About us',
      'PICK_A_MONTH': 'Pick a month'
    },
    'pl': {
      'CATEGORY_TITLE': 'Co wydarzylo sie w tym miesiacu?',
      'POSTED_IN': 'Wpis z kategorii ',
      'POSTED_ON': 'Wpis utworzony ',
      'CREATED_WHERE': 'Miejsce wydarzen: ',
      'ABOUT' : 'O nas',
      'PICK_A_MONTH': 'Wybierz miesiac'
    }
  }

IMAGE_PROCESS = {
    'crisp': {'type': 'responsive-image',
              'srcset': [('1x', ["scale_in 800 600 True"]),
                         ('2x', ["scale_in 1600 1200 True"]),
                         ('4x', ["scale_in 3200 2400 True"]),
                         ],
               'default': '1x',
             },
    'crisp-logo': {'type': 'responsive-image',
              'srcset': [('1x', ["scale_in 300 225 True"]),
                         ('2x', ["scale_in 400 300 True"]),
                         ('4x', ["scale_in 800 600 True"]),
                         ],
               'default': '1x',
             },
             
	'large-photo': {'type': 'responsive-image',
	   'sizes': '(min-width: 1200px) 800px, (min-width: 992px) 650px, \
	             (min-width: 768px) 718px, 100vw',
	   'srcset': [('600w', ["scale_in 600 450 True"]),
	              ('800w', ["scale_in 800 600 True"]),
	              ('1600w', ["scale_in 1600 1200 True"]),
	              ],
	    'default': '800w',
		},
    'about-image-90': {'type': 'image',
                      'ops': ["scale_in 300 300 True", "rotate 90"],
                      },
    'about-image-270': {'type': 'image',
                      'ops': ["scale_in 300 300 True", "rotate -90"],
                      }
    }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
