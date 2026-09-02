def permutation_maker(arr):
    res=[]
    sol=[]
    def backtracking(sol,res):
        if len(sol)==len(arr):
            res.append(sol[:])
            return
        for num in arr:
            if num not in sol:
                sol.append(num)
                backtracking(sol,res)
                sol.pop()
    backtracking(sol,res)
    return res
if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    print(permutation_maker(arr))