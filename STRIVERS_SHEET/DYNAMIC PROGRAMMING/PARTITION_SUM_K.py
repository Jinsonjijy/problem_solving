"""
Partition Equal Subset Sum (DP- 15)


3

Problem Description: Given an array arr of n integers, return true if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal else return false.

Examples
Input: nums = [2, 3, 3, 3, 4, 5]
Output: True
Explanation: Nums can be partitioned into two subsets of sum 10.


Input: nums = [1, 2, 3, 5]
Output: False
Explanation: The array cannot be partitioned into equal sum subsets
"""
def partition_sum(nums):
    total_sum=0
    for val in nums:
        total_sum+=val
    if total_sum%2!=0:
        return False
    target=total_sum/2
    def backtracking(ind,target):
        if ind==0:
            return nums[ind]==target
        if target==0:
            return True
        no_pick=backtracking(ind-1,target)
        pick=backtracking(ind-1,target-nums[ind]) if nums[ind]<=target else False
        return pick or no_pick
    return backtracking(len(nums)-1,target)
if __name__=="__main__":
    nums=list(map(int,input().split(" ")))
    print(partition_sum(nums))