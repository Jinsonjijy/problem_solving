"""Count digits in a number
Problem Statement: Given an integer N, return the number of digits in N."""
n=input("enter the number :")
count=0
for val in n:
    count+=1
print(count)
count1=0
m=int(n)
while m>0:
    m=m//10
    count1+=1
print(count1)