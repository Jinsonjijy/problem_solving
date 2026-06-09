"""Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False."""
arr=[1,2,4,5,36,7,9]
value=False
for i in range(len(arr)-1):
    if arr[i]<=arr[i+1]:
        value=True
    else:
        value=False
        break
print(value)