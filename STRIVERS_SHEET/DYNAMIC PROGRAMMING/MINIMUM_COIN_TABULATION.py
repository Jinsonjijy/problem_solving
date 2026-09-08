"""
Minimum Coins (DP - 20)


5

Problem Statement: Given an integer array of coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that are needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. There are infinite numbers of coins of each type

Examples
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1. We need 3 coins to make up the amount 11.
Input : coins = [2, 5], amount = 3
Output: -1
Explanation :  It's not possible to make amount 3 with coins 2 and 5. Since we can't combine the coin 2 and 5 to make the amount 3, the output is -1.

"""
if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    target=int(input("enter the target"))
    n=len(arr)
    dp=[[float("inf")]*(target+1) for _ in range(n)]
    for j in range(1,target+1):
        if arr[0]%j==0:
            dp[0][j] = j/arr[0]
    # for i in range(n):
    #     dp[i][0]=0
    for i in range(1,n):
        for j in range(0,target+1):
            no_take=0+dp[i-1][j]
            take=float("inf")
            if arr[i]<=j:
                take=1+dp[i][j-arr[i]]
            dp[i][j]=min(take,no_take)
    res=dp[n-1][target]
    if res==float("inf"):
        print(-1)
    else:
        print(int(res))