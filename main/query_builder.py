import datetime

stock_info_old = [('Avaya Holdings Corp', 'AVYA', '2017-12-19'), ('Alteryx Inc', 'AYX', '2017-03-24'), ('Cloudera Inc', 'CLDR', '2017-04-28'), ('ShotSpotter Inc', 'SSTI', '2017-06-07'), ('Appian Corporation', 'APPN', '2017-05-25'), ('Bandwidth Inc', 'BAND', '2017-11-10'), ('MongoDB Inc', 'MDB', '2017-10-19'), ('Micro Focus International', 'MFGP', '2017-08-17'), ('Okta Inc', 'OKTA', '2017-04-07'), ('Sailpoint Technologies Holdings Inc', 'SAIL', '2017-11-17'), ('Veritone Inc', 'VERI', '2017-05-12'), ('Yext Inc', 'YEXT', '2017-04-13'), ('Casa Systems', 'CASA', '2017-12-15'), ('Boxlight Corporation', 'BOXL', '2017-11-30'), ('Cambium Networks Corporation', 'CMBM', '2019-06-26'), ('Sonim Technologies Inc', 'SONM', '2019-05-10'), ('Smart Global Holdings Inc', 'SGH', '2017-05-24'), ('ACM Research Inc', 'ACMR', '2017-11-03')]

stock_info_new = [('Palantir', 'PLTR', '2020-09-30'), ('Asana', 'ASAN', '2020-09-30'), ('Snowflake', 'SNOW', '2020-09-16'), ('Kingsoft Cloud', 'KC', '2020-05-08'), ('ZoomInfo', 'ZI', '2020-06-03'), ('Unity', 'U', '2020-09-18')]

# run_loop = True

# while run_loop:
# 	company_name = str(input("Enter Company Name: "))
# 	ticker = str(input("Enter Ticker: "))
# 	ipo_date = str(input("Enter IPO Date: "))
# 	stock_info_new.append((company_name, ticker, ipo_date))
# 	run_loop = str(input("Would you like to conitnue? (Y/N): ")) == "Y"

# print(stock_info_new)

for company_name, ticker, ipo_date in stock_info_new:
	ipo_dt = datetime.datetime.fromisoformat(ipo_date)
	ipo_dt_str = ipo_dt.strftime('%Y-%m-%d')
	ipo_prev_one_day = ipo_dt - datetime.timedelta(days = 3)
	ipo_prev_one_day_str = ipo_prev_one_day.strftime('%Y-%m-%d')
	ipo_mkt_open = ipo_dt + datetime.timedelta(days = 1)
	ipo_mkt_open_str = ipo_mkt_open.strftime('%Y-%m-%d')
	print(f'(({company_name} OR "${ticker}") AND IPO) lang:en until:{ipo_dt_str} since:{ipo_prev_one_day_str} min_faves:1')

