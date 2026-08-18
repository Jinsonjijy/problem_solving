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
if __name__=="__main__":
    m=int(input("enter the row"))
    n=int(input("enter the coloumn"))
    arr=[]
    dict1={"name":"johan","age":18,"ph_no":None}
    # for i in range(m):
    #     row=list(map(int,input().split(" ")))
    #     arr.append(row)
    #     row=[]
    # print(**arr,sep="\n")
