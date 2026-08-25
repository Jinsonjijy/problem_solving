"""

Track
Command Palette
Search for a command to run...

Blog
Discussion
3-d DP : Ninja and his friends (DP-13)


4

Problem Statement:  We are given an ‘N*M’ matrix. Every cell of the matrix has some chocolates on it, mat[i][j] gives us the number of chocolates. We have two friends ‘Alice’ and ‘Bob’. initially, Alice is standing on the cell(0,0) and Bob is standing on the cell(0, M-1). Both of them can move only to the cells below them in these three directions: to the bottom cell (↓), to the bottom-right cell(↘), or to the bottom-left cell(↙). When Alica and Bob visit a cell, they take all the chocolates from that cell with them. It can happen that they visit the same cell, in that case, the chocolates need to be considered only once. They cannot go out of the boundary of the given matrix, we need to return the maximum number of chocolates that Bob and Alice can together collect.

Examples
Example 1:
Input: ‘R’ = 3, ‘C’ = 4
‘GRID’ = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
Output: 21

Example 2:
Input: ‘R’ = 2, ‘C’ = 3
‘GRID’ = [[4, 1, 2], [7, 3, 5]]
Output: 22

LEETCODE PROBLEM
1463. Cherry Pickup II
Hard
Topics
premium lock icon
Companies
Hint
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.

"""
def max_value_finding(arr):
    m=len(arr)
    n=len(arr[0])
    dp=[[-1]*n for _ in range(m)]
    def backtracking(i,j1,j2):
        if j1 < 0 or j1 >= n or j2 < 0 or j2 >= n:
            return float("-inf")
        if dp[i][j1]!=-1:
            
        if i==len(arr)-1:
            if j1==j2:
                return arr[i][j1]
            else:
                return arr[i][j1]+arr[i][j2]# this is the base case
        maxi=float("-inf")
        for di in [-1,0,1]:
            for dj in [-1,0,1]:
                if j1==j2:
                    ans=arr[i][j2]+backtracking(i+1,j1+di,j2+dj)
                else:
                    ans=arr[i][j1]+arr[i][j2]+backtracking(i+1,j1+di,j2+dj)
                maxi=max(maxi,ans)
        return maxi
    return backtracking(0,0,n-1)
if __name__=="__main__":
    arr=[]
    n=int(input("enter the row"))
    for i in range(n):
        row=list(map(int,input().split(" ")))
        arr.append(row)
        row=[]
    print(max_value_finding(arr))
