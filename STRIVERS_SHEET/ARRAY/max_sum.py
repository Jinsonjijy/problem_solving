"""

Kadane's Algorithm : Maximum Subarray Sum in an Array


36

Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.

A subarray is a contiguous non-empty sequence of elements within an array.

"""
nums = [-2, 3, 5, -2, 7, -4]
curr_sum=0
max_sum=nums[0]
for i in range(len(nums)):
    curr_sum+=nums[i]
    max_sum=max(max_sum,curr_sum)
    if curr_sum<0:
        curr_sum=0
print(max_sum)