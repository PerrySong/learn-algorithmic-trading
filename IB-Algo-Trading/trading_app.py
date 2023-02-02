# -*- coding: utf-8 -*-


from ibapi.client import EClient # Client to connect to TWS IBAPI
from ibapi.wrapper import EWrapper # Translate the TWS msg
from ibapi.contract import Contract
from ibapi.common import *
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
        # super().historicalData(reqId, bar)
        print("HistoricalData. ReqId: {}, Bar: = {}".format(reqId, bar))
        
    def historicalDataEnd(self, reqId: int, start: str, end: str):
        super().historicalDataEnd(reqId, start, end)
        print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)
        
    def historicalDataUpdate(self, reqId: int, bar: BarData):
        print("HistoricalDataUpdate. ReqId:", reqId, "BarData.", bar)

        
    # def reqHistoricalData(self, reqId:TickerId, contract:Contract, endDateTime:str,
    #                       durationStr:str, barSizeSetting:str, whatToShow:str,
    #                       useRTH:int, formatDate:int, keepUpToDate:bool, chartOptions:TagValueList):
    #     print("Calling reqHistoricalData...")
    #     super().reqHistoricalData(reqId, contract, endDateTime, durationStr, barSizeSetting, whatToShow, useRTH, formatDate, keepUpToDate, chartOptions)
    #     print("HistoricalData. ReqId: {}, Bar".format(reqId))
        