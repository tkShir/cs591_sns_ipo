# https://developer.twitter.com/en/docs
import json
import os
import datetime

import tweepy

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.join(DIR_PATH, "secrets/twitter_secrets.json")

# open a json file for reading and print content using json.load
with open(SECRET_FILE, "r") as content:
  TWITTER_SECRET = json.load(content)

auth = tweepy.OAuthHandler(TWITTER_SECRET["api_key"], TWITTER_SECRET["api_key_secret"])
auth.set_access_token(TWITTER_SECRET["acess_token"], TWITTER_SECRET["access_token_secret"])

api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search_full_archive,environment_name="IPOReception", query='Snowflake OR "$SNOW"', fromDate="202009130000", toDate="202009162359").items()

for status in tweets:
	print(type(status))
