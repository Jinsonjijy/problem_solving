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
if __name__=="__main__":
    coins=list(map(int,input().split(" ")))
    amt=int(input("target:"))
    n=len(coins)
    dp=[[0]*(amt+1) for _ in range(n)]
    for i in range(0,n):
        dp[i][0]=1
    for j in range(0,amt+1):
        if j%coins[0]==0:
            dp[0][j]=1

    for ind in range(1,n):
        for tar in range(0,amt+1):
            no_take=dp[ind-1][tar]
            take=0
            if coins[ind]<=tar:
                take=dp[ind][tar-coins[ind]]
            dp[ind][tar]=take+no_take
    print(dp[n-1][amt])