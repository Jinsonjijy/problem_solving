"""
Subset - II | Print all the Unique Subsets


5

Problem Statement: Given an integer array nums, which can have duplicate entries, provide the power set. Duplicate subsets cannot exist in the solution set. Return the answer in any sequence.

Examples
Input: array[] = [1,2,2]
Output: [ [ ],[1],[1,2],[1,2,2],[2],[2,2] ]
Explanation: We can have subsets ranging from  length 0 to 3. which are listed above. Also the subset [1,2] appears twice but is printed only once as we require only unique subsets.

Input: array[] = [1]
Output: [ [ ], [1] ]
Explanation: Only two unique subsets are available.

"""
def subset_2(arr):
    res=[]
    def backtracking(i,v,arr,n):
        if i==n:
            if v not in res:
                res.append(v[:])
            return
        v.append(arr[i])
        backtracking(i+1,v,arr,n)
        v.pop()
        backtracking(i+1,v,arr,n)
    backtracking(0,[],arr,len(arr))
    return res
arr= list(map(int,input().split(" ")))

print(subset_2(arr))