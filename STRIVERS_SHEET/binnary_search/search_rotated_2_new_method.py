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
def binnary_search(arr,target):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==target:#ultimate base condition always look this while looping
            return True
        if arr[l]==arr[mid]==arr[r]:
            l=l+1
            r=r-1
        elif arr[l]<=arr[mid]:#check in the left sorted array
            if arr[l]<=target<arr[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if arr[mid]<target<=arr[r]:
                l=mid+1
            else:
                r=mid-1
    return False


if __name__=="__main__":
    print("array:")
    arr=list(map(int,input().split(" ")))
    target=int(input())
    res=binnary_search(arr,target)
    print(res)

