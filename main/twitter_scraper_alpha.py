# https://developer.twitter.com/en/docs
import json
import os
import datetime

import tweepy


def get_api(DIR_PATH=None, SECRET_FILE_NAME=None):
	if DIR_PATH is None:
		DIR_PATH = os.path.dirname(os.path.abspath(__file__ + "../../"))
	if SECRET_FILE_NAME is None:
		SECRET_PATH = os.path.join(DIR_PATH, "secrets/twitter_secrets.json")
	else:
		SECRET_PATH = os.path.join(DIR_PATH, SECRET_FILE_NAME)

	
	# open a json file for reading and print content using json.load
	with open(SECRET_PATH, "r") as content:
  		TWITTER_SECRET = json.load(content)

	auth = tweepy.OAuthHandler(TWITTER_SECRET["api_key"], TWITTER_SECRET["api_key_secret"])
	auth.set_access_token(TWITTER_SECRET["acess_token"], TWITTER_SECRET["access_token_secret"])

	api = tweepy.API(auth)

	return api

def get_stock_data(api, company_name="Draft Kings", ticker="DKNG", ipo_date='2020-04-24'):
	# potentially add some filtering arguments

	# conver ipo_date into datetime for easier manipulation
	# currently: automatically set search range to one day before IPO to 2:30 PM (UTC) of the 
	#            day of IPO which is when the market open (although there might be some time
	#            lag between market open to actual listing
	
	ipo_dt = datetime.datetime.fromisoformat(ipo_date)
	ipo_prev_day = ipo_dt - datetime.timedelta(days = 5) + datetime.timedelta(hours=4)
	ipo_prev_day_str = ipo_prev_day.strftime('%Y%m%d%H%M')
	ipo_mkt_open = ipo_dt + datetime.timedelta(hours=13, minutes=30)
	ipo_mkt_open_str = ipo_mkt_open.strftime('%Y%m%d%H%M')

	tweets_items = tweepy.Cursor(api.search_full_archive,environment_name="StockDataLab", query=f'{company_name} OR "${ticker}"', fromDate=ipo_prev_day_str, toDate=ipo_mkt_open_str).items()
	
	status_count = 0
	for status in tweets_items:
		status_count += 1
		print("------------------------------")
		print(status)	
	print("------------------------------")
	print(status_count)

