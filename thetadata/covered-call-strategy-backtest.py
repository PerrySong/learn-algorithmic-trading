import pandas as pd
from datetime import date, timedelta
from thetadata import ThetaClient, OptionReqType, OptionRight, DateRange
from ratelimiter import RateLimiter




def end_of_day_option(symbol, start_date, end_date, exp_date, strike, client) -> pd.DataFrame:
    
    out = client.get_hist_option(
        req=OptionReqType.EOD,  # End of day data
        root=symbol,
        exp=exp_date,
        strike=strike,
        right=OptionRight.CALL,
        date_range=DateRange(start_date, end_date)
    )
    return out

def end_of_day_stock(symbol, start_date, end_date, client) -> pd.DataFrame:
    out = client.get_hist_stock(
        req=StockReqType.EOD,  # End of day data
        root=symbol,
        date_range=DateRange(start_date, end_date)
    )
    return out

def list_available_strikes(symbol, date, client):
    out = client.get_strikes(symbol, date, client)
    return out

def list_available_strikes(symbol, date, client):
    out = client.get_strikes()
    return out

def all_fridays(year):
    d = date(year, 1, 1)
    # First Friday
    d += timedelta(days = ((4 + 7) - d.weekday()) % 7)
    while d.year == year:
        yield d



if __name__ == "__main__":
    rate_limiter = RateLimiter(max_calls=18, period=60)
    # Make any requests for data inside this block. Requests made outside this block won't run.
    # Make the request
    client = ThetaClient()  # No credentials required for free access

    # List avaialbe strikes:
    with client.connect():
        for date in all_fridays(2022):
            with rate_limiter:
                print('date= ', date)
                strikes = client.get_strikes("SPY", date)
                print(type(strikes))
                break

    
    with client.connect():
        out = client.get_hist_stock(
            req=StockReqType.EOD,  # End of day data
            root="SPY",
            date_range=DateRange(date(2022, 1, 1), date(2023, 1, 1))
        )
        



    
    # We are out of the client.connect() block, so we can no longer make requests.