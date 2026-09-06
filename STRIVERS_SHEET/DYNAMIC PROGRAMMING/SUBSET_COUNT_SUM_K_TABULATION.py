"""
Count Subsets with Sum K (DP - 17)


3

Problem Statement : Given an array arr of n integers and an integer K, count the number of subsets of the given array that have a sum equal to K.

Examples
Input: arr = [1, 2, 2, 3], K = 3
Output: 3

Explanation: The subarrays [1,2], [1,2] and [3] have a sum of 3.
Input: arr = [1, 2, 3, 4, 5], K = 5
Output: 3
Explanation: The subsets are [5], [2, 3], and [1, 4]
"""
if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    n=len(arr)
    k=int(input("enter the target"))
    dp=[[0]*(k+1) for _ in range(n)]
    dp[0][0]=1
    if arr[0]<=k:
        dp[0][arr[0]]=1
    for i in range(1,n):
        for j in range(1,k+1):
            no_pick=dp[i-1][j]
            pick=0
            if arr[i]<=k:
                pick=dp[i-1][k-arr[i]]
            dp[i][j]=no_pick+pick
    print(dp[n-1][k])
