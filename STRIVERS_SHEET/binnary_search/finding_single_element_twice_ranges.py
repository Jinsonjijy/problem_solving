"""
224. Single element in sorted array
Given an array nums sorted in non-decreasing order. Every number in the array except one appears twice. Find the single number in the array.

Example 1:
Input :nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

Output:4

Explanation: Only the number 4 appears once in the array.

Example 2:
Input : nums = [1, 1, 3, 5, 5]

Output:3

Explanation: Only the number 3 appears once in the array.
    implemented it in O(lgn) times
    space complexity is O(1)
"""
def find_single(arr):
    l,r=0,len(arr)-1
    while l<r:
        mid=(l+r)//2
        if mid%2!=0:
            mid=mid-1
        if arr[mid]==arr[mid+1]:#pattern is correct check pattern distruption in right
            l=mid+2
        elif arr[mid]!=arr[mid+1]:#distruption happend
            r=mid
    return arr[l]


if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    res=find_single(arr)
    print(res)