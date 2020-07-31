#!/usr/bin/env python

import tweepy
# import datetime
# import re

import requests
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


consumer_key = 'Gm19gW2IgUjhaxwF833PuQeAJ'
consumer_secret = 'llLGAzbmgESlPDHBZUBIv2LmvYeBSlDQb40pjnJygwcHsoUOPe'
access_token = '1270971658862383104-QDQBlXBvdnn1FMgHISf1RqhgeA71HC'
access_token_secret = 'UTbDYDSE3Q3a5hKcabu1pMPJZ0NBLcjoitMlvctod8B5P'


API_ENDPOINT = "http://localhost:8888/createconv"
API_KEY = "XXXXXXXXXXXXXXXXX"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# token = session.get('request_token')
# session.delete('request_token')
# auth.request_token = token

# try:
#     auth.get_access_token(verifier)
# except tweepy.TweepError:
#     print ('Error! Failed to get access token.')


# try:
#     redirect_url = auth.get_authorization_url()
# except tweepy.TweepError:
#     print ('Error! Failed to get request token.')

auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# print(api)
users = ["986274664530952193"]

# def publictweet():
#     if datetime.date.today().weekday() == 0:
#         tweettopublish = 'Hi everyone, today is Monday.   #Monday '
#     if datetime.date.today().weekday() == 1:
#         tweettopublish = 'Enjoy your Tuesday.  #Tuesday'
#     if datetime.date.today().weekday() == 2:
#         tweettopublish = 'Third week of the Week. #Wednesday'
#     if datetime.date.today().weekday() == 3:
#         tweettopublish = 'Thursday. I cannot wait for the Weekend'
#     if datetime.date.today().weekday() == 4:
#         tweettopublish = 'Friday...Finally'
#     if datetime.date.today().weekday() == 5:
#         tweettopublish = 'Great it is Saturday #weekend #Saturday'
#     if datetime.date.today().weekday() == 6:
#         tweettopublish = 'Sunday morning...#Weekend #enjoy '
#
#     api.update_status(tweettopublish)
#     print(tweettopublish)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        print("init")
        # self.me = api.me()

    def on_status(self, tweet):
        # atlist  = re.findall("[@]\w+", tweet)
        # print(atlist)

        print("---")
        print("tweettext",tweet.text)
        print("tweetid:",tweet.id)
        print("user", {tweet.user.id_str}, {tweet.user.screen_name})


        print("replytotweetid:",{tweet.in_reply_to_status_id}, {tweet.in_reply_to_status_id_str})
        print("replytouserid", {tweet.in_reply_to_user_id},{tweet.in_reply_to_screen_name})

        if (tweet.user.id_str != tweet.in_reply_to_user_id_str):

            otweet = api.get_status(tweet.in_reply_to_status_id)
            print("original tweet:", otweet.text)
            print(f"{tweet.user.name}:{tweet.text}")

            data={
                "topic":otweet.text,
                "ouser":otweet.user.name,
                "user":tweet.user.name
            }

            r = requests.post(url = API_ENDPOINT, data = json.dumps(data))
            print(r.content)
            print(r.text)
            print(json.loads(r.text))
            rj = json.loads(r.text)
            fulllink = "http://app.manthanapp.com/join/"+rj["uid"]
            print(fulllink)

# r = requests.post(url = API_ENDPOINT, data = json.dumps(data))
# print(r.content)
# print(r.text)
# rj = json.loads(r.text)
# print(rj)
# print(rj["uid"])
# print("http://app1.immersmedia.in/join/"+rj["uid"])




            # m = "@%s, @%s Hello!, Have a great Manthan at %s" % (tweet.user.screen_name,tweet.in_reply_to_screen_name,fulllink)
            m = "@%s  @%s Hello!, Have a great Manthan at %s" % (tweet.in_reply_to_screen_name,tweet.user.screen_name,fulllink)
            # m = "Hello!, Have a great Manthan at %s" % (fulllink)
            # s = api.update_status(m, tweet.in_reply_to_status_id)
            s = api.update_status(m, tweet.id)
        else:
            a=20




    def on_error(self, status):
        print("Error detected")



tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
# stream.filter(track=["opynion_org"])
# stream.filter(follow=["986274664530952193"], async=True)
stream.filter(track=['letsmanthan'], is_async=True)

# mentions = api.mentions_timeline()
# for mention in mentions:
#     print("------")
#     print (mention.id, mention.author.screen_name, mention.text)

#tweets = api.mentions_timeline()
#for tweet in tweets:
#    tweet.favorite()
#    tweet.user.follow()
