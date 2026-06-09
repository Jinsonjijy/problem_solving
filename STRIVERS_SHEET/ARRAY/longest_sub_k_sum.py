"""
Count Subarray sum Equals K


20

Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k. A subarray is a contiguous non-empty sequence of elements within an array.

Examples
Input : N = 4, array[] = {3, 1, 2, 4}, k = 6
Output: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

Input: N = 3, array[] = {1,2,3}, k = 3
Output: 2
Explanation: The subarrays that sum up to 3 are [1, 2], and [3].


"""


arr=[3,1,2,4,6,1,5]
l=0
target=6
count=0
sum1=0
for r in range(len(arr)):
    sum1+=arr[r]
    while sum1>target:
        sum1-=arr[l]
        l+=1
    if sum1==target:
        count+=1
print(count)