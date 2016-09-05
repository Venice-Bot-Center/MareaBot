import tweepy

from mareabot import config

"""
Method to tweet on Twitter
"""


def tweet_status(status):
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(status=status)
