"""
Dynamic Programming: Frog Jump with k Distances (DP 4)


7

Problem Statement:

A frog wants to climb a staircase with n steps. Given an integer array heights, where heights[i] contains the height of the ith step, and an integer k. To jump from the ith step to the jth step, the frog requires abs(heights[i] - heights[j]) energy, where abs() denotes the absolute difference. The frog can jump from the ith step to any step in the range [i + 1, i + k], provided it exists. Return the minimum amount of energy required by the frog to go from the 0th step to the (n-1)th step.

Examples
Example 1:
Input: heights = [10, 5, 20, 0, 15], k = 2
Output: 15
Explanation:
0th step -> 2nd step, cost = abs(10 - 20) = 10
2nd step -> 4th step, cost = abs(20 - 15) = 5
Total cost = 10 + 5 = 15.

Example 2:
Input: heights = [15, 4, 1, 14, 15], k = 3
Output: 2
Explanation:
0th step -> 3rd step, cost = abs(15 - 14) = 1
3rd step -> 4th step, cost = abs(14 - 15) = 1
Total cost = 1 + 1 = 2.
 *make this index based
 * do all the stuffs in the index
 *take minimum energy so taking all the path and take minimum required
"""
def climbing_kth(height,k):
    dp=[-1]*(len(height)+1)
    def backtracking(ind,k):
        if ind==0:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        minimum=float("+inf")
        for jump in range(1,k+1):
            if ind-jump>=0:
                energy=abs(height[ind]-height[ind-jump])
                total=energy+backtracking(ind-jump,k)
                minimum=min(minimum,total)
        dp[ind]=minimum
        return dp[ind]
    return backtracking(len(height)-1,3)


if __name__=="__main__":
    heights=list(map(int,input().split(" ")))
    k=map(int,input())
    print(climbing_kth(heights,k))
