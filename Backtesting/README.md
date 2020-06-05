# Backtesting   

* Test the strategy by applying the rules and trading signal criteria on historical data mimicking actual trading conditions.   
* Factor in slippage, trading/brokerage cost when assessing the performance.   
* Be conservative - err on the side of caution.    
* Backtesting is of critical importance in assessing the merit of a trading strategy/system.   
* Don't deploy strategy in live market until back tested.   
* Criticism - Since it is based on historical data it has little predictive power

# Strategy 1 - Monthly Portfolio Rebalancing

* Chose any universe of stocks (Large cap, mid cap, small cap, industry specific, factor specific etc.) and stick to this group of stock as the source for your portfolio for the entire duration of backtesting.   

* Build fixed individual position sized long only portfolio by picking m number of stocks based on monthly returns (or any other suitable criterion).   

* Rebalance the portfolio every month by removing worse x stocks and replacing them with top x stocks from the universe of stocks (can existing stock be picked again?)

* Backtest the strategy and compare the KPIs with that of simple buy and hold strategy of corresponding index.