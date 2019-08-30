# api_config.py
'''Configuration file to help create API for programs based on the Tweepy Library '''
#
# NOTE: Reads in key variables from the environment for added security - initialize them via:
#
#    $ export CONSUMER_KEY=“{ADD_YOUR_KEY_HERE}”
#    $ export CONSUMER_SECRET="{ADD_CONSUMER_SECRET_HERE}"
#    $ export ACCESS_TOKEN="{ADD_YOUR_TOKEN_HERE}"
#    $ export ACCESS_TOKEN_SECRET="{ADD_YOUR_TOKEN_SECRET_HERE}"
# 
##########################################################################################

import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    ''' retrieves API keys, tokens, and secret values from environment and validates them'''
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API successfully created")
    return api
    
    
