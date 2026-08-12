"""
Maximum sum of non-adjacent elements (DP 5)


7

Problem Statement: Given an array of N positive integers, we need to return the maximum sum of the subsequence such that no two elements of the subsequence are adjacent elements in the array.

Note: A subsequence of an array is a list with elements of the array where some elements are deleted (or not deleted at all) and the elements should be in the same order in the subsequence as in the array.

Examples
Input: nums = [1, 2, 4]
Output: 5
Explanation:
Subsequence {1,4} gives maximum sum.

Input:  [2, 1, 4, 9]
Output: 11
Explanation:
Subsequence {2,9} gives maximum sum

"""
def subsequence(arr):
    dp=[-1]*len(arr)

    def backtracking(ind):
        if ind==0:
            return arr[ind]
        if ind<=1:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        pick=arr[ind]+backtracking(ind-2)
        no_pick=0+backtracking(ind-1)
        dp[ind]=max(pick,no_pick)
        return dp[ind]
    print(backtracking(len(arr)-1))
if __name__=="__main__":
    arr=list(map(int,input().split(",")))
    subsequence(arr)
