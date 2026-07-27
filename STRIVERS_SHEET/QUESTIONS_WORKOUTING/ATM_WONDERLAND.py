"""
There is a unique ATM in Wonderland. Imagine this ATM as an array of numbers. You can
withdraw cash only from either end of the array. Sarah wants to withdraw X amount of cash
from the ATM. What is the minimum number of withdrawals Sarah would need to accumulate
exactly X amount of cash? If it’s not possible, return -1.
Input Format: - First line: integer N (size of array) - Second line: N space-separated
integers (the ATM array) - Third line: integer X (target amount)
Output Format: - Minimum number of withdrawals, or -1

"""
no_cash=int(input())
cashes=list(map(int,input().split(" ")))
target=int(input())
dict1={}
count=1
for ind,val in enumerate(cashes):
    if target-val in dict:
        count+=1
    dict[val]=ind
if count>1:
    print(count)