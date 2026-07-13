"""
Combination Sum II - Find all unique combinations


5

Problem Statement: Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination..

Examples
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
Explanation: These are the unique combinations whose sum is equal to target

"""
def combination(arr,target):
    res=[]
    def backtracking(i,v,arr,n):
        if i>=n:
            if sum(v)==target:
                res.append(v[:])
            return
        v.append(arr[i])
        backtracking(i+1,v,arr,n)
        v.pop()
        backtracking(i+1,v,arr,n)

    backtracking(0,[],arr,len(arr))
    return res
arr=list(map(int,input().split(" ")))
target=int(input())
print(combination(arr,target))