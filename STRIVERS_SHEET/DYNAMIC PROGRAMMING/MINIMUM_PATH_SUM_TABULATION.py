"""

Minimum Path Sum In a Grid (DP 10)

Problem Statement: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Examples
Input: grid = [[5,9,6],[11,5,2]]
Output: 21
Explanation: Minimum sum is achieved via path 5->9->5->2 i.e. 21.

Input : grid = [[1,2,3],[4,5,6]]
Output: 12
Explanation : Minimum sum is achieved via path 1->2->3->6 i.e. 12
"""
if __name__=="__main__":
    arr=[]
    m=int(input("enter the row"))
    n=int(input("enter the coloumn"))
    for i in range(m):
        row=list(map(int,input().split(" ")))
        arr.append(row)
        row=[]
    dp=[[0]*n for _ in range(m)]
    print(*dp,sep="\n")
    dp[0][0]=arr[0][0]
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                continue
            else:
                up=arr[i][j]
                if i>0:
                    up+=dp[i-1][j]
                else:
                    up+=float("inf")
                left=arr[i][j]
                if j>0:
                    left+=dp[i][j-1]
                else:
                    left+=float("inf")
                    """  this is doing because when ever the pointer is at bounder it may take the min adjascent element not out of boundary"""
            dp[i][j]=min(up,left)


    print(dp[m-1][n-1])