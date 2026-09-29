"""
implementing upper bound
"""
def floor_ceil(arr,target):
    n=len(arr)
    l,r=0,n-1
    floor=-1
    ceil=-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==target:
            return arr[mid],arr[mid]
        elif arr[mid]<target:
            #finding the  floor which is lesser
            floor=arr[mid]
            l=mid+1 
            #checking any number on right  side which is greater
        else:
            ceil=arr[mid]
            r=mid-1
            # checking any value left side 
    return floor,ceil
arr=list(map(int,input().split(" ")))
target=int(input("target:"))
print(floor_ceil(arr,target))
