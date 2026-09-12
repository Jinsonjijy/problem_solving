"""
Rod Cutting Problem | (DP - 24)


6

Problem Statement: Given a rod of length N inches and an array price[] where price[i] denotes the value of a piece of rod of length i inches (1-based indexing). Determine the maximum value obtainable by cutting up the rod and selling the pieces. Make any number of cuts, or none at all, and sell the resulting pieces.

Examples

Input : price = [1, 6, 8, 9, 10, 19, 7, 20], N = 8
Output :25
Explanation :Cut the rod into lengths of 2 and 6 for a total price of 6 + 19= 25.

Input :price = [1, 5, 8, 9], N = 4
Output :10
Explanation :Cut the rod into lengths of 2 and 2 for a total price of 5 + 5 = 10.
"""
def max_cutting(prices):
    n=len(prices)
    def backtracking(ind,n):
        if ind==0:

            return n*prices[0]
        no_take=0+backtracking(ind-1,n)
        take=float("-inf")
        rod_lenght=ind+1
        if rod_lenght<=n:
            take=prices[ind]+backtracking(ind,n-rod_lenght)
        return max(take,no_take)
    return backtracking(n-1,n)
if __name__=="__main__":
    price=list(map(int,input().split(" ")))
    print(max_cutting(price))