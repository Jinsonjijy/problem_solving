""""
just creating a fibinocci number and then just finding out using memo first of all the
the top down approach in this file
"""
def fibinocci(n,dp):
    if n<=1:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=fibinocci(n-1,dp)+fibinocci(n-2,dp)
    return dp[n]
if __name__=="__main__":
    n=int(input())
    dp=[-1]*(n+1)
    print(fibinocci(n,dp))
