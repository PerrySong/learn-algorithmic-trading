## Slicing Dataframes

```python
  # Slice by row and column
  df[start_index : end_index, [col1, col2]]

  
  df.ix[] # More pythonic robust
```

## Plot a dataframe  

```python
  # Plot dataframe
  df1.plot()

  # Shows the plot in a window
  plt.show()

  # Normalize price data so that all prices start at 1.0
  df1 = df1 / df1[0]

  def plot_data(df, title='Stock price'):
    '''
    Plot stock prices
    '''
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show() # must be called to show plots in some environments
```

## Summary

1. Specify a set of dates using pandas.date_range.  
2. Creare an empty dataframe with dates as index. This helps align stock data and orders it by trading date.   
3. Read in a reference stock (here SPY) and drop non-trading days using pandas.DataFrame.dropna.  
4. Incrementally join dataframes using pandas.DataFrame.join.   
