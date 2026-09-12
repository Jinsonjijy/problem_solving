"""
518. Coin Change II
Medium
Topics
premium lock icon
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The final answer is guaranteed to fit into a signed 32-bit integer.



Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
"""
def count_coin(coin,amount):
    n=len(coin)
    dp=[[-1]*(amount+1) for _ in range(n)]
    def backtracking(ind,target):
        if target==0 :
            return 1
        if ind==0:
            if target % coin[ind]==0:
                return 1
            else:
                return 0
        if dp[ind][target]!=-1:
            return dp[ind][target]
        no_take=backtracking(ind-1,target)
        take=0
        if coin[ind]<=target:
            take=backtracking(ind,target-coin[ind])
        dp[ind][target] = take+no_take
        return dp[ind][target]
    return backtracking(n-1,amount)


if __name__=="__main__":
    coins=list(map(int,input().split(" ")))
    amount=int(input("enter the amount"))
    print(count_coin(coins,amount))