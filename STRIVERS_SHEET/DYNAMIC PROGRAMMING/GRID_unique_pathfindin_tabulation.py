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
if __name__=="__main__":
    m=int(input("enter the row"))
    n=int(input("enter the coloumn"))
    dp=[[0]*n for _ in range(m)]
    print(*dp,sep="\n")
    dp[0][0]=1
    count=0
    for i in range(0,m):
        for j in range(0,n):
            if i==0 and j==0:
                continue
            else:
                up=0
                left=0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
    print(dp[m-1][n-1])