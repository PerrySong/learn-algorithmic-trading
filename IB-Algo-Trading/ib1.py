# -*- coding: utf-8 -*-


from ibapi.client import EClient # Client to connect to TWS IBAPI
from ibapi.wrapper import EWrapper # Translate the TWS msg
from ibapi.contract import Contract
import threading
import time

class TradingApp(EWrapper, EClient): # Inherit 
    def __init__(self):
        EClient.__init__(self, self)
        
        
    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson = ""):
        print("Error {} {} {}".format(reqId, errorCode, errorString))
        
    
    def contractDetails(self, reqId, contractDetails):
    
        print("reqId: {}, contract: {}".format(reqId, contractDetails))
        



event = threading.Event()

    
app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=4)


def ws_conn():
    app.run()
    event.wait()
    if event.is_set():
        app.close()

conn_thread = threading.Thread(target=ws_conn)
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

    

event.set()