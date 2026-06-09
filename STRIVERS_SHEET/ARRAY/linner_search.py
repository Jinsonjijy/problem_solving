"""Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1."""
arr=list(map(int,input().split(" ")))
k=int(input())
flag=0
for val in arr:
    if val==k:
        print("value is found")
        flag=1
        break
    else:
        flag=0
if flag==0:
    print("value is not found")
