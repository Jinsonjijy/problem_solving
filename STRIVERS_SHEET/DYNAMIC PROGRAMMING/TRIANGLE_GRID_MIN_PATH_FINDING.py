"""
Minimum path sum in Triangular Grid (DP 11)


4

Problem Statement: Given a 2D integer array named triangle with n rows. Its first row has 1 element and each succeeding row has one more element in it than the row above it. Return the minimum falling path sum from the first row to the last.
Movement is allowed only to the bottom or bottom-right cell from the current cell.

Examples
Input: triangle = [[1], [1, 2], [1, 2, 4]]
Output: 3
Explanation: One possible route can be:
Start at 1st row -> bottom -> bottom.
Input : triangle = [[1], [4, 7], [4,10, 50], [-50, 5, 6, -100]]
Output: -42
Explanation : One possible route can be:
Start at 1st row -> bottom-right -> bottom-right -> bottom-right
"""
def min_path(arr):
    dp=[[-1]*len(arr) for _ in range(len(arr))]
    def backtracking(i,j):
        if i==len(arr)-1:
            return arr[i][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        d=arr[i][j]+backtracking(i+1,j)
        dg=arr[i][j]+backtracking(i+1,j+1)
        dp[i][j] = min(d,dg)
        return dp[i][j]
    return backtracking(0,0)
if __name__=="__main__":
    arr=[]
    n=int(input("enter the row"))
    for i in range(n):
        row=list(map(int,input().split(" ")))
        arr.append(row)
        row=[]
    print(min_path(arr))