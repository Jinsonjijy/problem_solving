"""
Given an array of integers, split them into two groups such that the absolute difference of
their sums is minimized. Print the two sums — smaller sum first, then larger sum.
Input Format: - First line: integer N - Second line: N space-separated integers
Output Format: - Two integers separated by space (smaller sum first)
Example:
Input:
4
1 5 3 8
Output:
8 9
Explanation: Group 1 = {1, 8} sum=9, Group 2 = {5, 3} sum=8. Or Group 1={1,3,5}=9,
Group 2={8}=8. Minimum difference is 1.
"""
def mini_diff(arr):
    res_dict={}
    def backtracking(i,v,arr,n):
        if i>=n:
            res_dict[sum(v)]=v[:]
            return
        v.append(arr[i])
        backtracking(i+1,v,arr,n)
        v.pop()
        backtracking(i+1,v,arr,n)
    backtracking(0,[],arr,len(arr))
    print(res_dict)
    res1=[]
    def backtracking_diff(i,v,arr,n,min_diff,prev_diff):
        if len(v)>=2:
            min_diff=min(min_diff,abs(v[0]-v[1]))
            if min_diff<=prev_diff:
                res1=v
            return
        v.append(arr[i])
        backtracking_diff(i+1,v,arr,n,min_diff,prev_diff)
        v.pop()
        backtracking_diff(i+1,v,arr,n,min_diff,prev_diff)
    backtracking_diff(0,[],list(res_dict.keys()),len(res_dict.keys()),float("+inf"),float("+inf"))
    return res1




arr=list(map(int,input().split(" ")))
mini_diff(arr)
