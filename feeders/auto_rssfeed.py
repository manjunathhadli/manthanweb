import sys
import tweepy
import json

import feedparser
# import BeautifulSoup
from bs4 import BeautifulSoup
import metadata_parser
# NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")

import requests
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


consumer_key = 'Gm19gW2IgUjhaxwF833PuQeAJ'
consumer_secret = 'llLGAzbmgESlPDHBZUBIv2LmvYeBSlDQb40pjnJygwcHsoUOPe'
access_token = '1270971658862383104-QDQBlXBvdnn1FMgHISf1RqhgeA71HC'
access_token_secret = 'UTbDYDSE3Q3a5hKcabu1pMPJZ0NBLcjoitMlvctod8B5P'

API_CF_ENDPOINT = "http://localhost:8888/createrssfeed"
API_KEY = "XXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)




feeds = ["https://www.thehindu.com/news/national/?service=rss",
        "https://indianexpress.com/feed/",
        "https://feeds.feedburner.com/ndtvnews-people",
        "http://www.firstpost.com/feed/rss",
        "https://www.dnaindia.com/feeds/india.xml",
        "https://www.livemint.com/rss/opinion"
        ]


for feed in feeds:
    NewsFeed = feedparser.parse(feed)

    # print (entry.keys())

    # print ('Number of RSS posts :', len(NewsFeed.entries))
    numentries = len(NewsFeed.entries)
    if (numentries > 0):
        # print(NewsFeed.entries[0])
        entry = NewsFeed.entries[0]
        data = {
            "title":entry["title"],
            "link":entry["link"],
        }

        # print (data)
        try:
            page = metadata_parser.MetadataParser(url=entry["link"])
        except:
            a = 21
        finally:
            if (page!=None):
                topic = page.get_metadatas('title', strategy=['og',])[0]
                imageurl = page.get_metadatas('image', strategy=['og',])[0]
                site_name  = page.get_metadatas('site_name', strategy=['og',])[0]
                url = page.get_metadatas('url', strategy=['og',])[0]

                data={
                    "topic":topic,
                    "imageurl":imageurl,
                    "site_name":site_name,
                    "url":url,
                    "author":site_name
                }

                r = requests.post(url = API_CF_ENDPOINT, data = json.dumps(data))
                print(r.content)

    # for entry in NewsFeed.entries:
    #     print (entry)

# entry = NewsFeed.entries[10]
# print ('Post :',entry)
# print ('Post Title :',entry.title)
