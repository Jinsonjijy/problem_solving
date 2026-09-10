"""
Target Sum (DP - 21)


1

Problem Statement: We are given an array ‘ARR’ of size ‘N’ and a number ‘Target’. Our task is to build an expression from the given array where we can place a ‘+’ or ‘-’ sign in front of an integer. We want to place a sign in front of every integer of the array and get our required target. We need to count the number of ways in which we can achieve our required target.

Examples
Input : nums = [1,1,1,1,1], target = 3
Output : 5
Explanation : There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Input : nums = [1], target = 1
Output : 1
Explanation : There is only one number, and we can assign a '+' sign to it to reach the target.
+1 = 1


"""
# this problem is same as the partition subarray count problem
def target_sum(nums,target):
    n=len(nums)
    total_sum=0
    for num in nums:
        total_sum+=num
    if abs(target)>total_sum:
        return 0
    if (total_sum+target)%2!=0:
        return 0
    s1=(total_sum+target)//2
    def backtracking(ind,s1):
        if ind==0:
            if s1==0 and nums[ind]==0:
                return 2
            if s1==0 or nums[ind]==s1:
                return 1
            return 0

        no_pick=backtracking(ind-1,s1)
        pick=0
        if nums[ind]<=s1:
            pick=backtracking(ind-1,s1-nums[ind])
        return pick+no_pick
    return backtracking(len(nums)-1,s1)
if __name__=="__main__":
    nums=list(map(int,input().split(" ")))
    target=int(input("target:"))
    print(target_sum(nums,target))