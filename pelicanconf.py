#!/usr/bin/env python
from __future__ import unicode_literals

import os

AUTHOR = u'fehiepsi'
SITENAME = u"fehiepsi's blog"
SITEURL = ''

# TIMEZONE = 'Europe/Paris'
TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)
LINKS =  (('binh yen', 'http://binhyen.livejournal.com/'),
          ('What\'s new', 'http://terrytao.wordpress.com/'),
          ('Zen Habits', 'http://zenhabits.net/'),
          ('A Quiet Place', 'http://genhara-chan.tumblr.com/'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
MENUITEMS = [('Archives', '/archives.html')]

# Github include settings
GITHUB_USER = 'fehiepsi'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# This requires Pelican 3.3+
STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
#  Theme requires http://github.com/duilio/pelican-octopress-theme/
#  Plugins require http://github.com/getpelican/pelican-plugins/
THEME = os.path.abspath('../pelican-octopress-theme/')
PLUGIN_PATH = '../pelican-plugins/'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
# 
# This header file is automatically generated by the notebook plugin
if not os.path.exists('./_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
    
# Sharing
TWITTER_USER = 'fehiepsi'
TWITTER_TWEET_BUTTON = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'

# RSS/Atom feeds
FEED_ATOM = 'atom.xml'

READERS = {'html': None}
