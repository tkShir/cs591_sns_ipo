import json
import os

def aggregate_json(ticker):
	JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__ + "../../")), f"output/{ticker}")
	
	count = 0
	res = {}
	for json_filename in os.listdir(JSON_PATH):
		json_path = os.path.join(JSON_PATH, json_filename)
		try:
			with open(json_path) as json_file:
				data = json.load(json_file)
		except:
			print(json_path)

		res[str(count)] = data
		count += 1

	SAVE_PATH = os.path.join(JSON_PATH, "master.json")
	with open(SAVE_PATH, 'w') as outfile:
			json.dump(res, outfile)

	print(count)