"""
next_permutation : find next lexicographically greater permutation


28

Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).
"""
nums=[2, 1, 5, 4, 3, 0, 0]
n=len(nums)
ind=-1# this is the breakpoint
for i in range(n-2,-1,-1):
    if nums[i]<nums[i+1]:
        ind=i #found the breakpoint index
        break

for i in range(n-1,ind,-1):
    if nums[i]>nums[ind]:
        nums[i],nums[ind]=nums[ind],nums[i]
        break
nums[ind+1:]=reversed(nums[ind+1:])

print(nums)