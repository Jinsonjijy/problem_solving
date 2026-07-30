"""
just creating a fibinocci program using the memoization

"""
def fibinocci(n,dp):
    if n<=1:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=fibinocci(n-1,dp)+fibinocci(n-2,dp)
    return dp[n]
n=int(input())
dp=[-1]*(n+1)
fibinocci(n,dp)
print(dp[n])
