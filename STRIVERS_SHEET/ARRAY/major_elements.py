"""
Problem Statement: Given an integer array nums of size n, return the majority element of the array.

The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.
"""
nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
hash_table={}
n=len(nums)
for val in nums:
    if val not in hash_table:
        hash_table[val]=1
    else:
        hash_table[val]+=1
for val in hash_table:
    if hash_table[val]>=n//2:
        print(val)
        break