"""
Check if there exists a subsequence with sum K


2

Problem Statement: Given an array nums and an integer k. Return true if there exist subsequences such that the sum of all elements in subsequences is equal to k else false.
"""
"""
Example 1:
Input :
 nums = [1, 2, 3, 4, 5] , k = 8
Output :
 Yes
Explanation :
 The subsequences like [1, 2, 5] , [1, 3, 4] , [3, 5] sum up to 8.

Example 2:
Input :
 nums = [4, 3, 9, 2] , k = 10
Output :
 No
Explanation :
 No subsequence can sum up to 10
"""
def subsequence(arr,x):
    res=[]
    def backtracking(i,v,x,arr,n,sum1):
        if i>=n:
            if sum1==x:
                return True
            return
        v.append(arr[i])
        if (backtracking(i+1,v,x,arr,n,sum1+arr[i]))==True:
            return True
        v.pop()
        if(backtracking(i+1,v,x,arr,n,sum1))==True:
            return True
    if(backtracking(0,[],x,arr,len(arr),0))==True:
        return "Yes"
    else:
        return "no"
    return res

arr=list(map(int,input().split(" ")))
target=int(input())
print(subsequence(arr,target))