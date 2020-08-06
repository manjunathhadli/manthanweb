# -*- coding: utf-8 -*-
import sys
import tweepy
import json

import requests
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


consumer_key = 'Gm19gW2IgUjhaxwF833PuQeAJ'
consumer_secret = 'llLGAzbmgESlPDHBZUBIv2LmvYeBSlDQb40pjnJygwcHsoUOPe'
access_token = '1270971658862383104-QDQBlXBvdnn1FMgHISf1RqhgeA71HC'
access_token_secret = 'UTbDYDSE3Q3a5hKcabu1pMPJZ0NBLcjoitMlvctod8B5P'

API_CF_ENDPOINT = "http://localhost:8888/createtwitterfeed"
API_KEY = "XXXXXXXXXXXXXXXXX"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Where On Earth ID for Brazil is 23424768.
INDIA_WOE_ID = 23424848

brazil_trends = api.trends_place(id = INDIA_WOE_ID)

trends = json.loads(json.dumps(brazil_trends, indent=1))
# print(trends)
index = 0
for trend in trends[0]["trends"]:
    index = index +1
    if (index > 2):
        break

	# print (trend["name"]).strip("#")
    print("---------------------------------")
    print (trend["name"])


    for tweet in tweepy.Cursor(api.search,q=trend["name"],count=3,
        lang="en",
        since="2020-08-05").items(5):
            print (tweet.created_at, tweet.text)
            data={
                "topic":tweet.text,
                "ouser":"",
                "user":tweet.user.name
            }

            r = requests.post(url = API_CF_ENDPOINT, data = json.dumps(data))
            print(r.content)
