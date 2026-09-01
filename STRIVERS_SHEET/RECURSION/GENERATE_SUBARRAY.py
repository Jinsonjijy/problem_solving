def subarray_generation(arr,k):
    res=[]
    def backtracking(i,v,arr,n):
        if i>=n:

            return
        v.append(arr[i])
        if sum(v[:])==k:
            res.append(v[:])
        backtracking(i+1,v,arr,n)
        v.pop()
    for i in range(len(arr)):
        backtracking(i, [], arr, len(arr))
    return res
if __name__=="__main__":
    print(subarray_generation([1,2,3],5))