# -*- coding: utf-8 -*-


from ibapi.client import EClient # Client to connect to TWS IBAPI
from ibapi.wrapper import EWrapper # Translate the TWS msg
from ibapi.contract import Contract
import threading
import time
import sys

class TradingApp(EWrapper, EClient): # Inherit 
    def __init__(self):
        EClient.__init__(self, self)
        
        
    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson = ""):
        print("Error {} {} {}".format(reqId, errorCode, errorString))
        
    
    def contractDetails(self, reqId, contractDetails):
    
        print("reqId: {}, contract: {}".format(reqId, contractDetails))
        
    def historicalData(self, reqId, bar):
        print("HistoricalData. ReqId: {}, Bar: {}".format(reqId, bar))
        

if __name__ == "__main__":
    
    app = TradingApp()
    app.connect("127.0.0.1", 7497, clientId=6)
    
    
    def ws_conn(event):
        app.run() # Blocking method until we call app.disconnect in a different thread
        print("app ran")
        event.wait()
        print("event wait completed")
        if event.is_set():
            app.disconnect()
            print('App closed')
            sys.exit()
    
    
    event = threading.Event()
    conn_thread = threading.Thread(target=ws_conn, args=(event,))
    conn_thread.start()
    
    print("Start")
    
    
    # Get contract info
    time.sleep(3)
    contract = Contract()
    contract.symbol = 'AAPL'
    contract.secType = 'STK'
    contract.currecy = 'USD'
    contract.exchange = 'SMART'
    
    app.reqContractDetails(102, contract)
    
    time.sleep(5)
    print("completed")
    print("setting event")
    app.disconnect()
    event.set()
    print("event set")
    time.sleep(5)