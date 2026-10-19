"""
62. Find minimum in Rotated Sorted Array
Given an integer array nums of size N, sorted in ascending order with distinct values, and then rotated an unknown number of times (between 1 and N), find the minimum element in the array.

Example 1:
Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]

Output: 0

Explanation: Here, the element 0 is the minimum element in the array.

Example 2:
Input : nums = [3, 4, 5, 1, 2]

Output: 1

Explanation:Here, the element 1 is the minimum element in the array
"""
def finding_min_rotated_arr(arr):
    l,r=0,len(arr)-1
    while l<r:
        mid=(l+r)//2
        if arr[mid]>arr[r]:
            l=mid+1
        else:
            r=mid
    return l

if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    res=finding_min_rotated_arr(arr)
    print(arr[res])