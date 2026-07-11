"""
Count all subsequences with sum K

Problem Statement: Given an array nums and an integer k.Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.


"""
def subsequence(arr,x):
    res=[]
    def backtracking(i,v,x,arr,n):
        if i>=n:
            if sum(v)==x:
                res.append(v.copy())
            return
        v.append(arr[i])
        backtracking(i+1,v,x,arr,n)
        v.pop()
        backtracking(i+1,v,x,arr,n)
    backtracking(0,[],x,arr,len(arr))
    return res

arr=list(map(int,input().split(" ")))
target=int(input())
print(subsequence(arr,target))