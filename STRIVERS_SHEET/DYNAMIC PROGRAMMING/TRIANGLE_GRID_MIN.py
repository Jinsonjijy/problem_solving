"""
Minimum path sum in Triangular Grid (DP 11)
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
if __name__=="__main__":
    arr=[]
    n=int(input("enter the row"))
    for i in range(n):
        row=list(map(int,input().split(" ")))
        arr.append(row)
        row=[]
    dp = [[0] * len(arr) for _ in range(len(arr))]
    for j in range(len(arr)):
        dp[len(arr) - 1][j] = arr[len(arr) - 1][j]
    for i in range(len(arr) - 2, -1, -1):
        for j in range(i, -1, -1):
            d = arr[i][j] + dp[i + 1][j]
            dg = arr[i][j] + dp[i + 1][j + 1]
            dp[i][j] = min(d, dg)
    print(dp[0][0])