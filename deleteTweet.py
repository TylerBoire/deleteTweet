#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import tweepy
from datetime import datetime, timedelta

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--tweets", help="Delete the Tweets", action='store_true')
parser.add_argument("-l", "--likes", help="Delete your likes", action='store_true')
parser.add_argument("-d", "--DM", help="Delete da DMs", action='store_true')
parser.add_argument("-k", "--keep", help="How many days to keep. Default 2", default=2)
parser.add_argument("-b" "--debug", help="Turn off debug mode", action='store_false')
args = parser.parse_args()

# Load your keys from https://apps.twitter.com/
# You must give the app permision to edit DMs if you want that functionality. 
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# Set on command line, or change permanently or shit wont work 
debugMode = True

days_to_keep = args.keep
cutoff_date = datetime.utcnow() - timedelta(days=days_to_keep)

def oauthLogin(consumer_key, consumer_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    
    verify_code = raw_input("Authenticate at %s and then enter you verification code here > " % auth_url) 
    auth.get_access_token(verify_code)
    
    return tweepy.API(auth)

def deleteStatus(api):
    for status in tweepy.Cursor(api.user_timeline).items():
        if status.id and status.created_at < cutoff_date:
            if debugMode and args.debug:
                print status.created_at
            else:
		api.destroy_status(status.id)

def deleteLikes(api):	
    for liked in tweepy.Cursor(api.favorites).items():
        if liked.created_at < cutoff_date:
            if debugMode and args.debug:
                print liked.created_at
            else:
		api.destroy_favorite(liked.id_str)
    
def deleteDM(api):
    for DM in tweepy.Cursor(api.sent_direct_messages).items():
        if DM.created_at < cutoff_date:
            if debugMode and args.debug:
                print DM.created_at
            else:
                api.destroy_direct_message(DM.id)

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    print "Authenticated as: %s" % api.me().screen_name
    if args.tweets:
        deleteStatus(api)
    if args.likes:
        deleteLikes(api)
    if args.DM:
        deleteDM(api)
