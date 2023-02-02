# -*- coding: utf-8 -*-

# Doc: https://interactivebrokers.github.io/tws-api/historical_data.html
from trading_app import TradingApp

from ibapi.client import EClient # Client to connect to TWS IBAPI
from ibapi.wrapper import EWrapper # Translate the TWS msg
from ibapi.contract import Contract
import threading
import time
import datetime

app = TradingApp()


if __name__ == "__main__":
    
    app = TradingApp()
    app.connect("127.0.0.1", 7497, clientId=11)
    
    def ws_conn(event):
        app.run() # Blocking method until we call app.disconnect in a different thread
        print("app stop running")
        event.wait()
        print("event wait completed")
        if event.is_set() and not app.isConnected():
            print('App closed')
            
    def ws_conn_daemon():
        app.run() # Blocking method until we call app.disconnect in a different thread
        print("app stop running")
        
            
            
    event = threading.Event()
    # conn_thread = threading.Thread(target=ws_conn, args=(event,))
    conn_thread = threading.Thread(target=ws_conn_daemon, daemon=True)
    conn_thread.start()
    
    print("Start trading app")
    
    contract = Contract()
    contract.symbol = 'META'
    contract.secType = 'STK'
    contract.currecy = 'USD'
    contract.exchange = 'SMART'
    
    
    print("Get historicalData")
    app.reqHistoricalData(reqId=4102, 
                          contract=contract, 
                          endDateTime='', 
                          durationStr="3 M", 
                          barSizeSetting="5 mins", 
                          whatToShow="ADJUSTED_LAST", 
                          useRTH=1, 
                          formatDate=1, 
                          keepUpToDate=False, 
                          chartOptions=[])


    time.sleep(5)
    print("completed")