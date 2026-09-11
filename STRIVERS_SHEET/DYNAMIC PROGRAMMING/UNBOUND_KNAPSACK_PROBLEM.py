"""
Unbounded Knapsack (DP-23)


5

Problem Statement: A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ items of infinite supply. Its weight is given by the ‘wt’ array and its value by the ‘val’ array. He can either include an item in its knapsack or exclude it but can’t partially have it as a fraction. We need to find the maximum value of items that the thief can steal. He can take a single item any number of times he wants and put it in his knapsack .

Examples

Input: n = 3, W = 8, wt = [2, 4, 6], val = [5, 11, 13]
Output: 22
Explanation:We can take item with weight 2 (value 5) four times to fill capacity 8,total value = 5 × 4 = 20.
But a better choice: take item with weight 2 (value 5) twice and item with weight 4 (value 11) once → total weight = 2 + 2 + 4 = 8, total value = 5 + 5 + 11 = 21.
Even better: take two items with weight 4 (value 11 each), total value = 22, which is maximum.

Input: n = 2, W = 3, wt = [2, 1], val = [4, 2]
Output: 6
Explanation:We can take item with weight 1 (value 2) three times , total value = 6.
Taking weight 2 (value 4) plus weight 1 (value 2) also gives 6. No combination yields more than 6.
"""
def unbound_knapsack(wt,val,bag):
    n=len(wt)
    dp=[[-1]*(bag+1) for _ in range(n)]

    def backtracking(ind,w):
        if w==0:
            return 0
        if ind ==0 :
            if wt[ind]<=w:
                return val[ind]*(w%wt[ind])
            else:
                return float("-inf")
        if dp[ind][w]!=-1:
            return dp[ind][w]
        no_take=0+backtracking(ind-1,w)
        take=float("-inf")
        if wt[ind]<=w:
            take=val[ind]+backtracking(ind,w-wt[ind])
        dp[ind][w] = max(take,no_take)
        return dp[ind][w]
    return  backtracking(n-1,bag)
if __name__=="__main__":
    wt=list(map(int,input().split(" ")))
    val=list(map(int,input().split(" ")))
    bag=int(input("bag_capacity:"))
    print(unbound_knapsack(wt,val,bag))