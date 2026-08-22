"""
213. House Robber II
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3


"""


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]

    nums1 = [nums[i] for i in range(1, len(nums))]
    nums2 = [nums[i] for i in range(0, len(nums) - 1)]
    dp = [-1] * len(nums)

    def backtracking(ind, numsn):
        if ind == 0:
            return numsn[0]
        if ind == 1:
            return max(numsn[0], numsn[1])
        if dp[ind] != -1:
            return dp[ind]
        pick = numsn[ind] + backtracking(ind - 2, numsn)
        no_pick = 0 + backtracking(ind - 1, numsn)
        dp[ind] = max(pick, no_pick)
        return dp[ind]

    max_value1 = backtracking(len(nums1) - 1, nums1)
    dp = [-1] * len(nums)
    max_value2 = backtracking(len(nums2) - 1, nums2)
    return max(max_value1, max_value2)
