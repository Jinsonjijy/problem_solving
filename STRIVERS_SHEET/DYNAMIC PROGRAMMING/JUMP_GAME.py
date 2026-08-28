"""
55. Jump Game
Attempted
Medium
Topics
premium lock icon
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


"""
def greedy_approach(arr):
    n=len(arr)
    far=0
    for i in range(n):
        if i>far:return False
        far=max(far,i+arr[i])
        if far>=n-1:
            return True
    return True



def finding_path(arr):
    n=len(arr)
    dp=[-1]*n
    def backtracking(ind):
        if ind>=n-1:
            return True
        if arr[ind]==0:
            return False
        if dp[ind]!=-1:
            return dp[ind]
        for i in range(1,arr[ind]+1):
            next_ind=ind+i
            if backtracking(next_ind):
                dp[ind]=True
                return True

        dp[ind]=False
        return False
    return backtracking(0)
if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    print(finding_path(arr))
    print(greedy_approach(arr))
