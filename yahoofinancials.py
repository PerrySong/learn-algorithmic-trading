#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:54:41 2020

@author: pengfeisong
"""

import pandas as pd
from yahoofinancials import YahooFinancials
import datetime as dt

all_tickers = ["APPL", "MSFT", "AMZN"]

ticker = 'MSFT'

yahoo_financials = YahooFinancials(ticker)

data = yahoo_financials.get_historical_price_data("2018-04-24", "2020-04-24", "daily")

# Parse the  json objectkl;
close_prices = pd.DataFrame()
end_date = (dt.date.today()).strftime('%Y-%m-%d')
beg_date = (dt.date.today() - dt.timedelta(1825)).strftime('%Y-%m-%d')
for ticker in all_tickers:
    yahoo_financials = YahooFinancials(ticker)
    json_obj = yahoo_financials.get_historical_price_data(beg_date,end_date,"daily")
    ohlv=json_obj[ticker]['prices']
    df = pd.DataFrame(ohlv)
    res = df[["adjclose"]]
    # temp = df[["formatted_date", "adjclose"]]
    # temp.set_index("formatted_date", inplace=True)
    # temp.dropna(inplace=True)
    # close_prices[ticker] = temp2["adjclose"]