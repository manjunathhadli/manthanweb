import tornado.ioloop
import tornado.web

import logging
import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.httpserver
import os.path
import uuid

from urlparse import parse_qs, urlparse
# import requests
import hashlib
import time
import json
import socket
import itertools
from urllib import quote
import os
import datetime
from datetime import timedelta
import sys
import HTMLParser
import re
import random
from tornado.template import Loader
from tornado.template import Template

import string


from tornado.concurrent import Future
from tornado import gen
from tornado.options import define, options



define("deploy", default="dev", help="deployment mode")
define("debug", default=False, help="run in debug mode")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def main():
    STATIC_DIRNAME = "static"
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), STATIC_DIRNAME),
        "static_url_prefix": "/.well-known/",
    }



    app = tornado.web.Application(
        [
            (r"/", MainHandler),
        ], **settings
#        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
#        template_path=os.path.join(os.path.dirname(__file__), "templates"),
#        static_path=os.path.join(os.path.dirname(__file__), "wellknown"),
#        xsrf_cookies=False,
#        debug=options.debug,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)

#    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
