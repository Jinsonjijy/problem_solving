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
import  time
def finding_longest(arr):
    n=len(arr)
    dp=[[-1]*(n+1) for _ in range(n)]
    def backtracking(ind,prev):
        if ind==n:
            return 0
        if dp[ind][prev]!=-1:
            return dp[ind][prev]
        skip=0+backtracking(ind+1,prev)
        pick=float("-inf")
        if prev ==-1 or arr[prev]<arr[ind]:
            pick=1+backtracking(ind+1,ind)
        dp[ind][prev] = max(pick,skip)
        return dp[ind][prev]
    return backtracking(0,-1)
if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    start_time=time.perf_counter()
    print(finding_longest(arr))
    end_time=time.perf_counter()
    print(f"{end_time-start_time:.2f}")