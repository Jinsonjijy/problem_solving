"""
Subset sum equal to target (DP- 14)


10

Problem Statement: We are given an array ‘ARR’ with N positive integers. We need to find if there is a subset in “ARR” with a sum equal to K. If there is, return true else return false.

A subset/subsequence is a contiguous or non-contiguous part of an array, where elements appear in the same order as the original array.
For example, for the array: [2,3,1] , the subsequences will be [{2},{3},{1},{2,3},{2,1},{3,1},{2,3,1}} but {3,2} is not a subsequence because its elements are not in the same order as the original array.

Examples

Input :  N = 4, ARR = [4, 3, 5, 2], K = 6
Output : true
Explanation : One possible subset with sum = 6 is [4, 2]. There’s also [3, 3] but that doesn’t exist in the array. As soon as we find one subset whose sum is equal to K, the answer is true.

Input : N = 3, ARR = [1, 2, 5], K = 4
Output : false
Explanation : Possible subsets and their sums: [1] → 1, [2] → 2, [5] → 5, [1,2] → 3, [1,5] → 6, [2,5] → 7, [1,2,5] → 8. None of them equal 4, so the answer is false

"""
# to implement the memoization we need a dp with the constrains as the limits
def subarray_sum_k(arr,k):
    dp=[[-1]*((10**3)+1) for _ in range((10**3)+1)]

    def backtracking(ind,target):
        if target ==arr[ind]:
            return True
        if ind==0:
            return arr[0]==target
        if dp[ind][target]!=-1:
            return dp[ind][target]
        no_take=backtracking(ind-1,target)
        take=backtracking(ind-1,target-arr[ind]) if arr[ind]<target else False
        dp[ind][target]= no_take or take
        return dp[ind][target]
    return backtracking(len(arr)-1,k)

if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    n=len(arr)
    k=int(input("enter the sum:"))
    print(subarray_sum_k(arr,k))