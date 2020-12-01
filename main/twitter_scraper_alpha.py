# https://developer.twitter.com/en/docs
import json
import os
import datetime
import json

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



def get_stock_data(api, company_name="Palantir", ticker="PLTR", ipo_date='2020-09-30', numTweets=100, DIR_PATH=None):
	# potentially add some filtering arguments

	if DIR_PATH is None:
		DIR_PATH = os.path.dirname(os.path.abspath(__file__ + "../../"))

	SAVE_PATH = os.path.join(DIR_PATH, f"output/{ticker}/")

	if not os.path.isdir(SAVE_PATH):
		os.mkdir(SAVE_PATH)


	# conver ipo_date into datetime for easier manipulation
	# currently: automatically set search range to one day before IPO to 2:30 PM (UTC) of the 
	#            day of IPO which is when the market open (although there might be some time
	#            lag between market open to actual listing
	
	ipo_dt = datetime.datetime.fromisoformat(ipo_date)
	ipo_two_prev_day = ipo_dt - datetime.timedelta(days = 1) + datetime.timedelta(hours=4)
	ipo_two_prev_day_str = ipo_two_prev_day.strftime('%Y%m%d%H%M')
	ipo_mkt_open = ipo_dt + datetime.timedelta(hours=13, minutes=30)
	ipo_mkt_open_str = ipo_mkt_open.strftime('%Y%m%d%H%M')

	query_str = f'({company_name} OR "${ticker}") IPO lang:en'

	tweets_items = tweepy.Cursor(api.search_full_archive,environment_name="pltrscrape", query=query_str, fromDate=ipo_two_prev_day_str, toDate=ipo_mkt_open_str, maxResults=numTweets).items(numTweets)
	
	status_count = 0
	for status in tweets_items:
		status_count += 1
		json_repr = status._json

		loc_save_path = os.path.join(SAVE_PATH, f'{status_count}.json')
		
		with open(loc_save_path, 'w') as outfile:
			json.dump(status._json, outfile)
	print(status_count)

def extend_scrape_results(api, prev_final_timestamp, company_name="Palantir", ticker="PLTR", ipo_date='2020-09-30', extend_by=100):
	DIR_PATH = os.path.dirname(os.path.abspath(__file__ + "../../"))
	SAVE_PATH = os.path.join(DIR_PATH, f"output/{ticker}/")

	prev_results = sorted(os.listdir(SAVE_PATH))
	if 'master.json' in prev_results:
		prev_results.remove('master.json')
	status_count = len(prev_results)

	prev_final_timestamp_str = prev_final_timestamp.strftime('%Y%m%d%H%M')
	adjusted_from = prev_final_timestamp - datetime.timedelta(days=2)
	adjusted_from_str = adjusted_from.strftime('%Y%m%d%H%M')

	print(prev_final_timestamp_str)
	print(adjusted_from_str)

	query_str = f'({company_name} OR "${ticker}") IPO lang:en'

	tweets_items = tweepy.Cursor(api.search_full_archive,environment_name="pltrscrape", query=query_str, fromDate=adjusted_from_str, toDate=prev_final_timestamp_str, maxResults=extend_by).items(extend_by)

	for status in tweets_items:
		status_count += 1
		json_repr = status._json

		loc_save_path = os.path.join(SAVE_PATH, f'{status_count}.json')

		with open(loc_save_path, 'w') as outfile:
			json.dump(status._json, outfile)
	print(status_count)