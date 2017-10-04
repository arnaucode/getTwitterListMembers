# coding=utf-8
import tweepy
import twitterConfig

# READ 'twitterConfigEXAMPLE.py' FOR THE CONFIGURATION INSTRUCTIONS

auth = tweepy.OAuthHandler(twitterConfig.consumer_key, twitterConfig.consumer_secret)
auth.set_access_token(twitterConfig.access_token_key, twitterConfig.access_token_secret)
api = tweepy.API(auth)


for member in tweepy.Cursor(api.list_members, twitterConfig.list_owner, twitterConfig.list_name).items():
    print member.screen_name + ',' + twitterConfig.list_owner
