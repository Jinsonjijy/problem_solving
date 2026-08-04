"""
Dynamic Programming : Frog Jump (DP 3)


10

Problem Statement: Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1..

Examples
Example 1:
Input: heights = [2, 1, 3, 5, 4]
Output: 2
Explanation: One possible route can be,
0th step -> 2nd Step = abs(2 - 3) = 1
2nd step -> 4th step = abs(3 - 4) = 1
Total = 1 + 1 = 2.

Example 2:
Input: heights = [7, 5, 1, 2, 6]
Output: 9
Explanation: One possible route can be,
0th step -> 1st Step = abs(7 - 5) = 2
1st step -> 3rd step = abs(5 - 2) = 3
3rd step -> 4th step = abs(2 - 6) = 4
Total = 2 + 3 + 4 = 9.


"""
def climbing(ind,height,dp):
    if ind==0:
        return 0
    if dp[ind]!=-1:
        return dp[ind]
    left=climbing(ind-1,height,dp)+abs(height[ind]-height[ind-1])
    right=float("+inf")
    if ind>1:
        right=climbing(ind-2,height,dp)+abs(height[ind]-height[ind-2])

    dp[ind] = min(left,right)
    return dp[ind]
if __name__=="__main__":
    height = list(map(int, input().split(", ")))
    dp=[-1]*len(height)
    print(climbing(len(height)-1,height,dp))