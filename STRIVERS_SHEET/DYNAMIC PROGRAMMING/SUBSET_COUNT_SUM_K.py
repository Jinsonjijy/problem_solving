"""
Count Subsets with Sum K (DP - 17)


3

Problem Statement : Given an array arr of n integers and an integer K, count the number of subsets of the given array that have a sum equal to K.

Examples
Input: arr = [1, 2, 2, 3], K = 3
Output: 3

Explanation: The subarrays [1,2], [1,2] and [3] have a sum of 3.
Input: arr = [1, 2, 3, 4, 5], K = 5
Output: 3
Explanation: The subsets are [5], [2, 3], and [1, 4]
"""
def count_subarray(arr,k):
    dp=[[-1]*(k+1) for _ in range(len(arr))]
    n=len(arr)
    def backtracking(ind,target):
        if target==0:
            return 1
        if ind==0:
            if arr[ind]==target:
                return 1
            else:
                return 0
        if dp[ind][target]!=-1:
            return dp[ind][target]

        no_pick=backtracking(ind-1,target)
        pick=0
        if arr[ind]<=target:
            pick=backtracking(ind-1,target-arr[ind])
        dp[ind][target] = pick+no_pick
        return dp[ind][target]
    return backtracking(n-1,k)
if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    k=int(input("enter the sum:"))
    print(count_subarray(arr,k))
