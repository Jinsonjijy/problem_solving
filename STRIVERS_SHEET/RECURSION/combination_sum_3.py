"""
Combination Sum II - Find all unique combinations


5

Problem Statement: Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used not only once in the combination..

Examples this i example is just used but we are using the element multiple times to get the answer
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]]
Explanation: These are the unique combinations whose sum is equal to target.

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
Explanation: These are the unique combinations whose sum is equal to target.
"""
def combinations(arr,target):
    res=[]
    def backtracking(i,rem,v):
        if rem==0:
            res.append(v[:])
            return
        if i==len(arr):
            return
        if arr[i]<=rem:
            v.append(arr[i])
            backtracking(i,rem-arr[i],v)
            v.pop()
        backtracking(i+1,rem,v)
    backtracking(0,target,[])
    return res

arr=list(map(int,input().split(" ")))
target=int(input())
print(combinations(arr,target))