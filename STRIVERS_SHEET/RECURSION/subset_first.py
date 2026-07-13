"""
Subset Sum : Sum of all Subsets


7

Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.

Examples

Input: N = 3, arr[] = {5,2,1}
Output: 0,1,2,3,5,6,7,8
Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],so the sums we get will be  0,1,2,3,5,6,7,8

Input: N=3,arr[]= {3,1,2}
Output: 0,1,2,3,3,4,5,6
Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [3], [3,1], [3,2]. [3,2,1],so the sums we get will be  0,1,2,3,3,4,5,6
"""
def subset(arr):
    res=[]
    def backtracking(i,v,arr,n):
        if i==n:
            res.append(v[:])
            return
        v.append(arr[i])
        backtracking(i+1,v,arr,n)
        v.pop()
        backtracking(i+1,v,arr,n)
    backtracking(0,[],arr,len(arr))
    return res
arr=list(map(int,input().split(" ")))
print("subsets of the arr:\n",subset(arr))