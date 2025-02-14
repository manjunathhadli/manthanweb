import tornado.ioloop
import tornado.web

import logging
import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.httpserver
import os.path
import uuid

# import requests
import hashlib
import time
import json
import socket
import itertools
import os
import datetime
from datetime import timedelta
import sys
# import HTMLParser
import re
import random
from tornado.template import Loader
from tornado.template import Template

import string


from tornado.concurrent import Future
from tornado import gen
from tornado.options import define, options

# from google.cloud import firestore
#==========================
# import config
import debateclass
import constants
import bfeedclass
# =========================
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

os.sys.path.append(os.environ['MANTHANWEB_HOME'])

cred = credentials.Certificate(os.environ['MANTHANWEB_HOME']+'/Certificate.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

twitterpic = "https://app.manthanapp.com/static/assets/images/twitterlogoblue.png"
twitterurl = "https://www.twitter.com"


define("deploy", default="dev", help="deployment mode")
define("debug", default=False, help="run in debug mode")

class joindebview(tornado.web.RequestHandler):
    def get(self, url):
        o = urlparse(self.request.uri)
        p = o.path.split('/')
        uid = p[2]
        hashuser = o.query
        print(uid)

        self.render("join.html")

class createtwitterconv(tornado.web.RequestHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        print(data)
        topic = data["topic"]
        ouser = data["ouser"]
        user = data["user"]



        uid = str(uuid.uuid4())
        feeduid = str(uuid.uuid4())

        ts = datetime.datetime.now()
        userstring  = ouser+"/"+user
        feed = bfeedclass.bfeed(feeduid,topic,userstring,"Twitter",twitterpic,twitterurl)
        feed.convos.append(uid)
        print(feed.to_dict())

        conv = debateclass.debate(uid,topic,ts)
        conv.feeduid = feeduid
        print(conv.to_dict())

        db.collection(constants.FB_RCOLL_DEBATES).document(uid).set(conv.to_dict())
        db.collection(constants.FB_RCOLL_ALLFEED).document(feeduid).set(feed.to_dict())
        # db.collection(u'test').document(uid).set(conv.to_dict())

        retdata = {
            "status": "success",
            "uid":uid
        }
        self.write(retdata)
        return

class createtwitterfeed(tornado.web.RequestHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        print(data)
        topic = data["topic"]
        ouser = data["ouser"]
        user = data["user"]

        feeduid = str(uuid.uuid4())
        ts = datetime.datetime.now()
        userstring  = ouser+"/"+user
        feed = bfeedclass.bfeed(feeduid,topic,userstring,"Twitter",twitterpic,twitterurl)

        print(feed.to_dict())

        db.collection(constants.FB_RCOLL_ALLFEED).document(feeduid).set(feed.to_dict())

        retdata = {
            "status": "success",
            "uid":feeduid
        }
        self.write(retdata)
        return

class createrssfeed(tornado.web.RequestHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        print(data)
        topic = data["topic"]
        imageurl = data["imageurl"]
        site_name = data["site_name"]
        pageurl = data["url"]
        author = data["author"]

        feeduid = str(uuid.uuid4())
        ts = datetime.datetime.now()
        userstring  = author
        feed = bfeedclass.bfeed(feeduid,topic,author,site_name,imageurl,pageurl)

        print(feed.to_dict())

        db.collection(constants.FB_RCOLL_ALLFEED).document(feeduid).set(feed.to_dict())

        retdata = {
            "status": "success",
            "uid":feeduid
        }
        self.write(retdata)
        return

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
            (r"/createtwitterconv", createtwitterconv),
            (r"/createtwitterfeed", createtwitterfeed),
            (r"/createrssfeed", createrssfeed),
            (r"/join/(.*)", joindebview),
        ], **settings
#        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
#        template_path=os.path.join(os.path.dirname(__file__), "templates"),
#        static_path=os.path.join(os.path.dirname(__file__), "wellknown"),
#        xsrf_cookies=False,
#        debug=options.debug,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    # http_server.listen(80)

#    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
