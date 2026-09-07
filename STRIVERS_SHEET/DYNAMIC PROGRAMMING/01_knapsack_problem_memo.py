"""

0 - 1 Knapsack Problem
Difficulty: MediumAccuracy: 31.76%Submissions: 617K+Points: 4
Given two arrays, val[] and wt[], where each element represents the value and weight of an item respectively, and an integer W representing the maximum capacity of the knapsack (the total weight it can hold).
Put the items into the knapsack such that the total value obtained is maximum without exceeding the capacity W.

Note: You can either include an item completely or exclude it entirely — fractional selection of items is not allowed. Each item is available only once.

Examples :

Input: W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1]
Output: 3
Explanation: Choose the last item, which weighs 1 unit and has a value of 3.
Input: W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6]
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).
Input: W = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 2, 3]
Output: 80
Explanation: Choose the third item (value 30, weight 2) and the last item (value 50, weight 3) for a total value of 80.
"""
def kanpsack(val,wt,w):
    def backtracking(ind,w):
        if ind==0:
            if wt[0]<=w:
                return val[0]
            else:
                return 0
        if dp[ind][w]!=-1:
            return dp[ind][w]
        no_pick=0+backtracking(ind-1,w)
        pick=float("-inf")
        if wt[ind]<=w:
            pick=val[ind]+backtracking(ind-1,w-wt[ind])
        dp[ind][w] = max(pick,no_pick)
        return dp[ind][w]
    return backtracking(n-1,w)
if __name__=="__main__":
    val=list(map(int,input().split(" ")))
    wt=list(map(int,input().split(" ")))
    w=int(input("enter the weight of bag:"))
    print(kanpsack(val,wt,w))