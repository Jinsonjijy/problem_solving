"""
    implementing the first occurance ans last occurance of a array
    quick point is define two binnary search one for first and which look for left side
    another binnary search which is for last in the right side
"""
def first_find(arr,target):
    n=len(arr)
    l=0
    r=n-1
    first=0
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==target:
            first=mid
            r=mid-1
        elif arr[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return first
def second_find(arr,target):
    l,r=0,len(arr)-1
    second=0
    while l<=r:
        mid=(l+r)//2
        if arr[mid] == target:
            second=mid
            l=mid+1
        elif arr[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return second
if __name__=="__main__":

    arr=list(map(int,input().split(" ")))
    target=int(input())
    first=first_find(arr,target)
    second=second_find(arr,target)
    print(first,second)