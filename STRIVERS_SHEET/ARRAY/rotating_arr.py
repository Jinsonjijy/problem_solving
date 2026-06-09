"""Rotate array by K elements


31

Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right"""
arr=list(map(int,input().split(" ")))# this give you input split and make it a int list
k=int(input("enter the number of rotation:"))
k=k%len(arr)
for i in range(k):
    data=arr.pop(0)
    arr.append(data)
print(arr)
