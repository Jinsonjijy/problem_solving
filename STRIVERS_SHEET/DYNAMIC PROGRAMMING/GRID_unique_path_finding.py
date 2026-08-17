"""
Grid Unique Paths : DP on Grids (DP8)


2

Problem Statement: Given two integers m and n, representing the number of rows and columns of a 2d array named matrix. Return the number of unique ways to go from the top-left cell (matrix[0][0]) to the bottom-right cell (matrix[m-1][n-1]).

Movement is allowed only in two directions from a cell: right and bottom.

Examples
Example 1:
Input:
 m = 3, n = 2
Output:
 3
Explanation:
 There are 3 unique ways to go from the top-left to the bottom-right cell:
1) right → down → down
2) down → right → down
3) down → down → right

Example 2:
Input:
 m = 2, n = 4
Output:
 4
Explanation:
 There are 4 unique ways to go from the top-left to the bottom-right cell:
1) down → right → right → right
2) right → down → right → right
3) right → right → down → right
4) right → right → right → down


"""
def pathfinding(m,n):
    dp=[[-1]*n for _ in range(m)]
    def backtracking(ind,next,dp):
        if ind==0 and next ==0:
            return 1
        if ind<0 or next<0:
            return 0
        if dp[ind][next]!=-1:
            return dp[ind][next]
        up = backtracking(ind-1,next,dp)
        left = backtracking(ind,next-1,dp)
        dp[ind][next] = up+left
        return dp[ind][next]
    return backtracking(m-1,n-1,dp)

if __name__=="__main__":
    m=int(input("enter the rows"))
    n=int(input("enter the coloumns"))
    print(pathfinding(m,n))

