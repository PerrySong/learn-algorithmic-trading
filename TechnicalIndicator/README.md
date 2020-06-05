# Technical Indicators:   
are mathematical calculations based on historic price, volume or open interest information to predict asset price direction.

* Fundamental part of technical analysis which is based on analyzing trends, chart patterns, price action etc.   

* Different from fundamental analysis in that this approach is indifferent about stock's financials or operational details since Efficient Market Hypothesis contends that all information is already priced in by the market.    

* Popular technical indicators include:  
1. MACD: Moving Average Convergence Divergence  
2. Bollinger Bands    
3. RSI: Relative Strength Index   
4. ADX: Average Directional Index   
5. Supertrend   
6. Renko Charts   

## MACD: Moving Average Convergence Divergence

* It is a trend following momentum indicator which is calculated by taking the difference of two moving averages of an asset price (typically 12 period MA and 26 period MA).   

* A signal line is also calculated which is again a moving average (typically 9 period) of the MACD line calculated as per the above step.

* The MACD line cutting the signal line from below signals bullish period and the former cutting the latter from above signals bearish period. This is called crossover strategy.

* Many false positives - especially during sideways market.   

* Suggested that this indicator be used in conjunction with other indicators.    

* Lagging indicator: Trails behind the actual price action

## Bollinger Bands & ATR (Average True Range)   

* Both Bollinger bands and ATR are volatility based indicators  

* Bollinger band comprises of two lines plotted n (n is typically 2) standard deviations from a m period simple moving average line (m is typically 20); The bands widen during periods of increased volatility and shrink during period of reduced volatility.

* The ATR takes in account the market movement each day in either direction and averaging them out. It focuses on total price movement and conveys how wildly the market is swinging as it moves.

* Traders typically use them in conjunction as they approach volatility diferently and are complimentary.

## RSI - Relative Strength Index   

* RSI is a momentum oscillator which measures the speed and change of price movements.   

* RSI value oscillates between 0 and 100 with values above 70 indicating that the asset has now reached overbought territory. Values below 30 signify oversold territory.   

* Assets can remain in overbought and oversold territories for long durations.   

* Calculation follows a two step method wherein the second step acts as a smoothening technique (similar to calculating exponential MA).   

RSI (step one) = 100 - (100 / (1 + (Ave Gain / Ave Loss)))   

RSI (step two) = 100 - (100 / (1 + ((Prev Ave Gain * 13 + Current Gain) / (Prev Ave Loss * 13 + Current Loss))))   

## ADX (Average Directional Index)   

* ADX is a way of measuring the strength of a trend.   

* Values range from 0 to 100 and quantifies the strength of a trend as per below:  
  1. 0-25: Absent or weak trend.   
  2. 25-50: Strong trend.   
  3. 50-75: Very strong trend.   
  4. 75-100: Extremely strong trend.   

* ADX is non directional meaning the ADX value makes no inference about the direction of the trend but only about the strength of the trend.   

* The calculation involves finding both positive and negative directional movement (by comparing successive highs and successive lows) and then calculating the smoothed average of the difference of these.   

### ADX Formula   

* TR (True Range): Max(today's high - today's low, abs(today's high - yesterday's close), abs(today's low - yesterday's close))

* DM+ (Directional Movement): if(today's high - yesterday's high > yesterday's low - today's low) ? MAX(today's high - yesterday's high, 0) : 0

* DM- (Directional Movement): if(yesterday's low - today's low > today's high - yesterday's high) ? MAX(yesterday's low - today's low, 0) : 0

* TR14(14 period): SUM(TRi: i = [n - 13, n])
* DM+_14: SUM(DM+: (i - 13 ~ i))
* DM-_14: SUM(DM-: (i - 13 ~ i))

* DI+ (Directional indicator): 100 * (DM+_14 / TR) 

* DI- : 100 * (DM-_14 / TR)

* DI+_Sum: (DI+) + (DI-) 
* DI+_Diff: abs((DI+) - (DI-))
* DX (Direction Index): 100 * (DI+_Diff / DI+_Sum)
* ADX (Average Direction Index): avg(DXi: (i = [n - 13, n])) 

## OBV (On Balance Volume )

* OBV is a momentum indicator which uses changes in trading volume as an indicator of future asset price moves.   

* OBV formulation is based on the theory that volume precedes price movement. A rising OBV reflects positive volume pressure that can lead to higher prices and falling OBV predicts decline in prices.   

* Leading market indicator but prone to making false signals. Typically used in conjunction with lagging indicators such as MACD.

* The calculation of OBV is fairly straightforward and it is simply the cumulative sum of volume treaded adjusted for the direction of the corresponding asset price move.

OBC = OBV(prev) + (close == close(prev) ? 0 : close > close(prev) ? volume : -volume).


## Slopes   
Visualization, see slop.py

## Renko Chart   

* Renko chart is built using price movement and not price against standardized time intervals - This filters out the noise and lets you visualize the true trend.

* Price movements (fixed) are represented as bricks stacked at 45 degrees to each other. A new brick is added to the chart only when the price moves by a predetermined amount in either direction.

* Renko charts have a time axis, but the time scale is not fixed. Some bricks may take longer to form than others, depending on how long it takes the price to move the required box size.

* Renko charts typically use only the closing price based on the chart time frame chosen.

## TA lib   

Is a technical analysis library (link)[https://mrjbq7.github.io/ta-lib/]

* Pattern Recognition
* Not a perfect library

* TODO: figure out how to install the package

Otherwise, you can only implement your own pattern recognition function.

