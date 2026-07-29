"""
normal implementation of the binnary search

"""
def binnary_search(arr,target):
    l=0
    r=len(arr)
    while l<r:
        mid=(l+r)//2
        if arr[mid]==target:
            return mid+1
        elif arr[mid]<target:
            l=mid+1
        elif arr[mid]>target:
            r=mid-1
    return -11
arr=list(map(int,input().split(" ")))
target=int(input())
print(binnary_search(arr,target))
print()