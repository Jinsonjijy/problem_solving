"""Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array."""
arr=[2,4,5,6,7,8,9,10]
target=7
l,r=0,len(arr)
while l<r:
    mid=(l+r)//2
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid]<target:
        l=mid+1
    elif arr[mid]>target:
        r=mid-1
