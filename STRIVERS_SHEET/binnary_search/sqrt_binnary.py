""""
just finding the sqrt function using the binnary search algorithm
"""
def sqrt_fun(num):
    l=0
    r=num
    while l<=r:
        mid=(l+r)//2
        if mid**2==num:
            return mid
        elif mid**2<num:
            l=mid+1
        elif mid**2>num:
            r=mid-1
    return -1
num=int(input())
print(sqrt_fun(num))