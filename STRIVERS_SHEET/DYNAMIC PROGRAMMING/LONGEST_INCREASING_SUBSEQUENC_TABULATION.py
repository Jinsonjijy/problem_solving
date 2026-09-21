"""
300. Longest Increasing Subsequence
Medium
Topics
premium lock icon
Companies
Given an integer array nums, return the length of the longest strictly increasing subsequence.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""
import time
if __name__=="__main__":
    start_time=time.perf_counter()
    arr=list(map(int,input().split(" ")))
    n=len(arr)
    dp=[[0]*(n+1) for _ in range(n+1)]
    for ind in range(n-1,-1,-1):
        for prev in range(ind-1,-2,-1):
            skip=0+dp[ind+1][prev+1]
            pick=float("-inf")
            if prev ==-1 or arr[prev]<arr[ind]:
                pick=1+dp[ind+1][ind+1]
            dp[ind][prev+1]=max(pick,skip)
    end_time=time.perf_counter()
    print(dp[0][0])
    print(f"time:{end_time-start_time}")