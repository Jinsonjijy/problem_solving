"""

112. Search in rotated sorted array-II
Given an integer array nums, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.

Example 1:
Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3

Output: True

Explanation: The element 3 is present in the array. So, the answer is True.

Example 2:
Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10

Output: False

Explanation:The element 10 is not present in the array. So, the answer is False
"""
from binnary_search.FIRST_LAST_occurance import first_find
from binnary_search.find_index import target


def binnary_search(arr,target):
    l,r=0,len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return None
if __name__=="__main__":
    print("enter array")
    arr=list(map(int,input().split(" ")))
    print("enter target")
    k=int(input())
    split=0
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            split=i+1

    first_arr=arr[:split]
    second_arr=arr[split:]
    if len(first_arr) == 0:
        normal_find=binnary_search(arr,k)
        if normal_find is not None:
            print(True)
        else:
            print(False)
    else:
        find_first=binnary_search(first_arr,k)
        if find_first is not None:
            print(True)
        else:
            find_second = binnary_search(second_arr, k)
            if find_second is not None:
                print(True)
            else:
                print(False)


