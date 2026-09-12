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
if __name__=="__main__":
    price=list(map(int,input().split(" ")))
    N=len(price)
    dp=[[0]*(N+1) for _ in range(N)]
    for i in range(1,N+1):
        dp[0][i]=price[0]*i
    for ind in range(1,N):
        for j in range(1,N+1):
            no_take=0+dp[ind-1][j]
            piece_lenght=ind+1
            take=0
            if piece_lenght<=j:
                take=price[ind]+dp[ind][j-piece_lenght]
            dp[ind][j]=max(take,no_take)
    print(dp[N-1][N])

