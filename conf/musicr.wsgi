#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/")

from musicr import musicr
application = musicr.app

application.secret_key = 'mon_key_mon'