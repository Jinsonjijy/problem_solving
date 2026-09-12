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
""" in this i am also stress testing my pc ram usage for this computation 
example:
   wt: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
   val:3 7 12 15 20 24 28 31 35 39 42 47 50 55 59 63 68 71 76 80
    target:5000000
"""
import time
if __name__=="__main__":
    wt=list(map(int,input().split(" ")))
    val=list(map(int,input().split(" ")))
    bag=int(input("bag capacity"))
    n=len(wt)
    start_time=time.perf_counter()
    dp=[[0]*(bag+1) for _ in range(n)]
    for w in range(bag+1):
        if wt[0]<=w:
            dp[0][w]=val[0]*(w//wt[0])
    for ind in range(1,n):
        for w in range(0,bag+1):
            no_take=dp[ind-1][w]
            take=0
            if wt[ind]<=w:
                take=val[ind]+dp[ind][w-wt[ind]]
            dp[ind][w]=max(take,no_take)
    end_time=time.perf_counter()
    total_time=end_time-start_time
    print("maximum is :",dp[n-1][bag])
    print(f" total time requiered : {total_time:.6f} seconds")