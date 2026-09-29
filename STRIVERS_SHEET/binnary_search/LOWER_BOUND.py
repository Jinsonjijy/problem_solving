"""
IMPLEMENTING LOWER BOUND VALUE FROM A SORTED ARRAY
"""
def lower_bound(arr,target):
    l=0
    r=len(arr)-1
    ans=0
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>=target:
            ans=arr[mid]
            r=mid-1
        else:
            l=mid+1
    return ans
arr=list(map(int,input().split(" ")))
target=int(input("target:"))
print(lower_bound(arr,target))
