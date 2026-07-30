"""
this file is just using the normal tabulation method like building up from the
base case and then return the result that is the basic idea
just like "brick by brick"
"""
import fibinocci_function

n=int(input())

print(fibinocci_function.fibinocci(n,[-1]*(n+1)))
if __name__=="__main__":
    dp=[-1]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    print(dp[n])
