"""
Suppose we could access yesterday's stock prices as a list, where:

The values are the price in dollars of Apple stock.
A higher index indicates a later time.
So if the stock cost $500 at 10:30am and $550 at 11:00am, then:

stock_prices_yesterday[60] = 500

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
"""

def get_max_profit(prices):
    # write the body of your function here
    if not prices: # check we have stock value
        return 0

    max_value = max(prices)
    max_index = prices.index(max_value)
    search_list = prices[:max_index]

    if not search_list: # check for negative decreasing values
        return 0
    min_value = min(search_list)

    if min_value >= max_value: # no negatves
        return 0

    return max_value - min_value

# run your function through some test cases here
# remember: debugging is half the battle!

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# get_max_profit(stock_prices_yesterday)
# get max index
# find min before


print get_max_profit(stock_prices_yesterday)
