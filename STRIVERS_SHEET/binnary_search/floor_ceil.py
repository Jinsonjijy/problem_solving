"""
implementing upper bound
"""
def upper_bound(arr,target):
    n=len(arr)
    l,r=0,n-1
    ans=-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>target:
            ans=arr[mid]
            r=mid-1
        else:
            l=mid+1
    return ans