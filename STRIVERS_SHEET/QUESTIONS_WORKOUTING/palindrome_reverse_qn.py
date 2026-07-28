"""
Problem Statement:
Given a number N, check if the sum of N and its reverse is a palindrome. If yes, print the
palindrome sum. If no, print “Not Palindrome”.
Input Format: - Single integer N
Output Format: - The palindrome sum, or “Not Palindrome”
Example:
Input:
124
Output:
545


"""
n=int(input())
temp=n
res=0
while n>0:
    num=n%10
    res=res*10+num
    n=n//10
print(res)
sum1=res+temp
temp2=sum1
res1=0
while sum1>0:
    num1=sum1%10
    res1=res1*10+num1
    sum1=sum1//10
if res1==temp2:
    print(res1)
else:
    print("NO")