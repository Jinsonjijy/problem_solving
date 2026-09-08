"""
Minimum Coins (DP - 20)


5

Problem Statement: Given an integer array of coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that are needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. There are infinite numbers of coins of each type

Examples
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1. We need 3 coins to make up the amount 11.
Input : coins = [2, 5], amount = 3
Output: -1
Explanation :  It's not possible to make amount 3 with coins 2 and 5. Since we can't combine the coin 2 and 5 to make the amount 3, the output is -1.
"""
from Scripts.unicodedata import normalize


def minimum_coin(nums,target):
    dp=[[-1]]
    n=len(arr)
    def backtracking(ind,target):
        if ind==0:
            if target%nums[ind]==0:
                return target//nums[ind]
            else:
                return float("inf")
        no_take=0+backtracking(ind-1,target)
        take=float("inf")
        if nums[ind]<=target:
            take=1+backtracking(ind,target-nums[ind])
        return min(take,no_take)
    return backtracking(n-1,target)
if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    target=int(input("enter the target:"))
    print(minimum_coin(arr,target))
