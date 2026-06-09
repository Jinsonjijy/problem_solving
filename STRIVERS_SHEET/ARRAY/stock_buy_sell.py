"""
Stock Buy And Sell


15

Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note: That buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


"""
# prices = [7,1,5,3,6,4]
# n=len(prices)
# profit=float('-inf')
# max_profit=float("-inf")
# for i in range(n-1):
#     profit=max(prices[i+1:])-prices[i]
#     max_profit=max(max_profit,profit)
# print(max_profit)
"""
this is the optimal approach
prices = [7,1,5,3,6,4]

min_price = prices[0]
max_profit = 0

for price in prices:
    min_price = min(min_price, price)
    profit = price - min_price
    max_profit = max(max_profit, profit)

print(max_profit)
"""
prices = [7,1,15,3,6,4]
min_price=prices[0]
max_profit=0
for price in prices:
    min_price=min(min_price,price)
    profit=price-min_price
    max_profit=max(max_profit,profit)
print(max_profit)
