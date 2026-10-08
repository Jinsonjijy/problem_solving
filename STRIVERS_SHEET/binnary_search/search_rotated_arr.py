"""
46. Search in rotated sorted array-I
Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.

Example 1:
Input : nums = [4, 5, 6, 7, 0, 1, 2], k = 0

Output: 4

Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

Example 2:
Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3

Output: -1

Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.

"""
def binnary_search(arr,k):
    l,r=0,len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            l=mid+1
        else:
            r=mid-1
    return -1

if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    k=int(input("target:"))
    first_arr=[]
    second_arr=[]
    split=0
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            split=i+1

    first_arr=arr[:split]
    second_arr=arr[split:]

    first_arr_ind=binnary_search(arr[:split],k)

    if first_arr_ind!=-1:
        print(first_arr_ind)
    else:
        second_arr_ind = binnary_search(arr[split:], k)
        if second_arr_ind!=-1:
            print(second_arr_ind+split)
        else:
            print(-1)
