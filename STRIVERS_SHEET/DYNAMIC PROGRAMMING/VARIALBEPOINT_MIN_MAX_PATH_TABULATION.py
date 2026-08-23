# """"""
# this is a varibale starting point and varible end Problem
# def path_finding(arr):

def min_pathfinding(arr):
    dp=[[0]*len(arr[0]) for _ in range(len(arr))]
    for j in range(len(arr[0])):
        dp[0][j] = arr[0][j]
    for i in range(1, len(arr)):
        for j in range(0, len(arr[0])):
            ul = 0
            ur = 0
            up = 0
            up = arr[i][j] + dp[i - 1][j]
            if j - 1 >= 0:
                ul = arr[i][j] + dp[i - 1][j - 1]
            else:
                ul += float("inf")
            if j + 1 < len(arr[0]):
                ur = arr[i][j] + dp[i - 1][j + 1]
            else:
                ur += float("inf")
            dp[i][j] = min(up, min(ul, ur))
    mini = float("inf")
    for j in range(0, len(dp[0])):
        mini = min(mini, dp[len(arr) - 1][j])
    return mini