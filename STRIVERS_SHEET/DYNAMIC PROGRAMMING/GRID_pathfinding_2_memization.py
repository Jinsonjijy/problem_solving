"""
Grid Unique Paths 2 (DP 9)


1

Problem Statement: Given an m x n 2d array named matrix, where each cell is either 0 or 1. Return the number of unique ways to go from the top-left cell (matrix[0][0]) to the bottom-right cell (matrix[m-1][n-1]). A cell is blocked if its value is 1, and no path is possible through that cell.

Movement is allowed in only two directions from a cell - right and bottom.

Examples
Example 1:
Input:
 matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
Output:
 2
Explanation:

The two possible paths to reach the bottom-right cell are:
1) down → down → right → right
2) right → right → down → down
Thus, the number of paths is 2.

Example 2:
Input:
 matrix = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
Output:
 0
Explanation:
 There is no valid path to reach the bottom-right cell due to blocked cells (represented by 1).


"""
def pathfinding(arr):
    dp=[[-1]*len(arr[0]) for _ in range(len(arr))]
    def backtracking(ind,next):
        if arr[ind][next] == 1:
            return 0
        if ind==0 and next ==0:
            return 1 #their is a slight change we need to make  make sure the first base should be wheather it is 0 or 1 if the first value is 1 we cannot do anything just return 0
        if ind<0 or next <0:
            return 0
        if dp[ind][next]!=-1:
            return dp[ind][next]
        if arr[ind][next]==0:
            up=backtracking(ind-1,next)
            left=backtracking(ind,next-1)
            dp[ind][next] = up+left
            return dp[ind][next]
    return backtracking(len(arr)-1,len(arr[0])-1)    
if __name__=="__main__":
    m=int(input("enter the row"))
    n=int(input("enter the coloumn"))
    arr=[]
    for i in range(m):
        row=list(map(int,input().split(" ")))
        arr.append(row)
        row=[]
    print(*arr,sep="\n")
    print(pathfinding(arr))
    