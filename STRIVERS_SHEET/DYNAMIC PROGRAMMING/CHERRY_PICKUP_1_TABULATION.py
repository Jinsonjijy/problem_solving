"""
741. Cherry Pickup
Hard
Topics
premium lock icon
Companies
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.


Example 1:


Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
Output: 5
Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
Example 2:

Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
Output: 0
this is a tabulation method
"""
def cherry_pack(arr):
    n=len(arr)
    dp=[[[0]*n for _ in range(n)]for _ in range(n)]

    dp[n-1][n-1][n-1]=arr[n-1][n-1]
    for i1 in range(n-2,-1,-1):
        for j1 in range(n-1,-1,-1):
            for i2 in range(n-1,-1,-1):
                if i1==n-1 and j1==n-1 and i2==n-1:
                    continue
                j2=i1+j1-i2
                if i1==i2 and j1==j2:
                    cherry=arr[i1][j1]
                else:
                    cherry=arr[i1][j1]+arr[i2][j2]
                    # lets write the combination
                dd=dp[i1+1][j1][i2+1] if i1+1 >


if __name__=="__main__":
    n=int(input("enter the row"))
    arr=[]
    for i in range(3):
        row=list(map(int,input().split(" ")))
        arr.append(row)
        row=[]
    print(*arr,sep="\n")
