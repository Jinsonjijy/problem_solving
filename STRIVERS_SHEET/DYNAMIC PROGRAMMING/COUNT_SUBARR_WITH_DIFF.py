"""

Count Partitions with Given Difference (DP - 18)


3

Problem Statement : Given an array with N positive integers and an integer D, count the number of ways we can partition the given array into two subsets, S1 and S2 such that S1 - S2 = D and S1 is always greater than or equal to S2.

Examples
Input: arr = [1, 1, 2, 3], diff = 1
Output: 3
Explanation: The subsets are [1, 2] and [1, 3], [1, 3] and [1, 2], [1, 1, 2] and [3].
Input:  arr = [1, 2, 3, 4], diff = 2
Output: 2
Explanation: The subsets are [1, 3] and [2, 4], [1, 2, 3] and [4].
"""
def count_subbarrray_with_given_diff(nums,d):
    total_sum=0
    for val in nums:
        total_sum+=val
    s1=(d+total_sum)//2
    def backtracking(ind,target):
        if target == 0:
            return 1
        if ind==0:
            return nums[ind]==target
        no_pick=backtracking(ind-1,target)
        pick=0
        if nums[ind]<=target:
            pick=backtracking(ind-1,target-nums[ind])
        return pick+no_pick
    return backtracking(len(nums)-1,s1)


if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    d=int(input("enter the diff:"))
    print(count_subbarrray_with_given_diff(arr,d))
