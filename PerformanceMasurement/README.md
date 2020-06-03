# Performance Measurement

* Measuring performance of a trading strategy is of critical importance.

* Various key performance indicators (KPIs) used to measure both risk and return characteristic of strategy

* Popular performance measures include:
  1. Cumulative Annual Growth Rate
  2. Annualized Volatility (Standard Deviation)
  3. Sharpe Ratio / Sortino Ratio
  4. Maximum Drawdown
  5. Calmar Ratio

## CAGR (Compounded Annual Growth Rate)

* Compounded Annual Growth Rate is the annual rate of return realized by an asset/portfolio to reach its current market value from its initial value.

* CAGR calculation assumes profits are continuously reinvested.
  CAGR = (End value / Beginning value) ^ (1 / years) - 1

* Provides ease of comparison between different trading strategies.

* Does not reflect investment risk and therefore should always be used in conjunction with a volatiliy measure.

## Annualized Volatility

* Volatility of a strategy is represented by the standard deviation of the returns. This captures the variability of returns from the mean return.

* Annualization is achieved by multiplying volatility with square root of the annualization factor. For example:

1. To annualize daily volatility multiply with square_root(252) - 252 trading days in a year.   
2. To annualize weekly volatility multiply with square_root(52) - 52 trading weeks in a year.   
3. To annualize monthly volatility multiply with square_root(12) - 12 trading month in a year.   

* Widely used measure of risk. However, this approach assumes normal distribution of returns which is not true.   

* Does not capture tail risk.   

## Sharpe Ratio & Sortino Ratio

* Sharpe ratio is the average return earned in excess of the risk free rate per unit of volatility.   
* Widely used measure of risk adjusted return.     
* Investors pay close attention to this metric when comparing funds.   
* Sharpe ratio greater than 1 is considered good, greater than 2 very good and greater than 3 excellent.  

Sharpe Ratio = (Rp - Rf) / (σp) 
1. Rp = Expected Return   
2. Rf = Risk Free rate of return  
3. σp = Standard Deviation of volatility  

## Sortino Ratio

* Sortino Ratio is a variation of Sharpe ratio which takes into account standard deviation of only negative returns.    
* One of the criticism of Sharpe ratio is that it fails to distinguish between upside and downside fluctuation, Sortino makes than distinction and therefore considers only harmful volatility.


