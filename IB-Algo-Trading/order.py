# -*- coding: utf-8 -*-

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time
import pandas as pd

# {0:[{open,high,low,close},{}] 1:...}
class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        self.data = {}
        
    def historicalData(self, reqId, bar):
        if reqId not in self.data:    
            self.data[reqId] = [{"Date": bar.date, "Open": bar.open, "High": bar.high, "Low": bar.low}]
        
        else:
            self.data[reqId].append({"Date": bar.date, "Open": bar.open, "High": bar.high, "Low": bar.low})
            
        print("HistoricalData. ReqId:", reqId, "BarData.", bar)
        

def websocket_con():
    app.run()
    


 
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

# starting a separate daemon thread to execute the websocket connection
con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) # some latency added to ensure that the connection is established


def us_tech_stk(symbol, sec_tyoe="STK", currency="USD", exchange="ISLAND"):
    
    #creating object of the Contract class - will be used as a parameter for other function calls
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_tyoe
    contract.currency = currency
    contract.exchange = exchange
    return contract

def hist_data(req_num, contract, duration, candle_size):
    print("Getting hist_data")
    app.reqHistoricalData(reqId=req_num, 
                          contract=contract,
                          endDateTime='',
                          durationStr='3 M',
                          barSizeSetting='5 mins',
                          whatToShow='ADJUSTED_LAST',
                          useRTH=1,
                          formatDate=1,
                          keepUpToDate=0,
                          chartOptions=[])


##################### Storing  data into dataframe #######################

def to_data_frame(tradeapp_obj, tickers):
    df_dict = {}
    for ticker in tickers:
        df_dict[ticker] = pd.DataFrame(tradeapp_obj[tickers.index(ticker)])
        df_dict[ticker].set_index("Date", inplace=True)
        
    return df_dict


### Order ###

order = Order()


tickers = ["META", "AMZN", "INTC"]


starttime = time.time()
timeout = starttime + 60*5

while time.time() <= timeout:
    
    for ticker in tickers:
        hist_data(tickers.index(ticker), us_tech_stk(ticker), '3600 S', '30 secs')
        time.sleep(3) # some latency added to ensure that the contract details request has been processed

    to_data_frame(app, tickers)
    time.sleep(30 - (time.time() - starttime) % 30)