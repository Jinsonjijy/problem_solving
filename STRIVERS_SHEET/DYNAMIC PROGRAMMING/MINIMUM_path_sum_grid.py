"""

Minimum Path Sum In a Grid (DP 10)


0

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
def min_path(arr):
    sum1=0
    def backtracking(ind,next,sum1):
        if ind==0 and next ==0:
            sum1+=arr[0][0]
            return sum1
        if ind<0 or next <0:
            return 0
        if arr[ind-1][next]<arr[ind][next-1]:
            sum1+=arr[ind][next]
            return backtracking(ind-1,next,sum1)
        elif arr[ind-1][next]>arr[ind][next-1]:

            sum1+=arr[ind][next]
            return backtracking(ind,next-1,sum1)
    return backtracking(len(arr)-1,len(arr[0])-1,sum1)

if __name__=="__main__":
    m=int(input("enter the row"))
    n=int(input("enter the coloumn"))

    arr=[]
    for i in range(m):
        row=list(map(int,input().split(" ")))
        arr.append(row)
        row=[]
    print(*arr,sep="\n")
    print(min_path(arr))