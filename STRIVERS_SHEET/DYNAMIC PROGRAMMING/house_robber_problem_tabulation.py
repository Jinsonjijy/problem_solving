from HOUSE_ROBBERS_2 import rob
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
if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    dp=[0]*len(arr)
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(2,len(arr)):
        pick=arr[i]+dp[i-2] #if we take the curr element the we also take i-2th element so it wont be adjascent
        no_pick=dp[i-1] #if we dont take the curr elelent then take previous element
        dp[i]=max(pick,no_pick)
    print(dp[len(arr)-1])
    print(rob(arr))# this is the memoization method calling of house_robber_problem_2