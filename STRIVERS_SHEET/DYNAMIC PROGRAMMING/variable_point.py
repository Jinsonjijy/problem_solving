# """"""
# this is a varibale starting point and varible end Problem
# def path_finding(arr):

def max_path_finding(arr):
    dp=[[-1]*len(arr[0]) for _ in range(len(arr))]
    def backtracking(i,j):
        if j<0 or j>=len(arr[0]):
            return float("-inf")
        if i==0:
            return arr[0][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        ul=arr[i][j]+backtracking(i-1,j-1)
        u=arr[i][j]+backtracking(i-1,j)
        ur=arr[i][j]+backtracking(i-1,j+1)
        dp[i][j]=max(ul,max(u,ur))
        return dp[i][j]
    maxi=float("-inf")
    for j in range(len(arr[0])):
        max1=backtracking(len(arr)-1,j)
        maxi=max(maxi,max1)
    return maxi
if __name__=="__main__":
    
    n=int(input("enter the row"))
    arr=[]
    for i in range(n):
        row=list(map(int,input().split(" ")))
        arr.append(row)
        row=[]
    print(*arr,sep="\n")
    print(max_path_finding(arr))