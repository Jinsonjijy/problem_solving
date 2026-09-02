"""
2035. Partition Array Into Two Arrays to Minimize Sum Difference
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

Return the minimum possible absolute difference.



Example 1:

example-1
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
Example 2:

Input: nums = [-36,36]
Output: 72
Explanation: One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
Example 3:

example-3
Input: nums = [2,-1,0,4,-2,-9]
Output: 0
Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.
"""
def minimum_diff_subarray(arr):
    total_sum=sum(arr)
    n=len(arr)
    dp=[[False]*(total_sum+1) for _ in range(n)]
    for i in range(n):
        dp[i][0]=True
    if arr[0]<=total_sum:
        dp[0][arr[0]]=True
    for i in range(1,n):
        for target in range(1,total_sum+1):
            take=False
            if arr[i]<=target:
                take =  dp[i-1][target-arr[i]]
            no_take=dp[i-1][target]
            dp[i][target]=take or no_take
    # now we are implementing the logic of code kindly look the book if you get any confusion
    mini=float("inf")
    for s1 in range(0,total_sum+1):
        if dp[n-1][s1]==True:
            s2=total_sum-s1
            mini=min(mini,abs(s2-s1))
    return mini



if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    print(minimum_diff_subarray(arr))
