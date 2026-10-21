"""
839. Count Occurrences in a Sorted Array
You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.

Return the count of occurrences of target in the array.

Example 1:
Input: arr = [0, 0, 1, 1, 1, 2, 3], target = 1

Output: 3

Explanation: The number 1 appears 3 times in the array.

Example 2:
Input: arr = [5, 5, 5, 5, 5, 5], target = 5

Output: 6

Explanation: All elements in the array are 5, so the target appears 6 times
"""
def find_occurance(arr,target,isright):
    l,r=0,len(arr)-1
    ind=-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==target:
            ind=mid
            if isright == True:
                l=mid+1
            else:
                r=mid-1
        elif arr[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return ind


if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    target=int(input())
    first_ind=find_occurance(arr,target,False)
    second_ind=find_occurance(arr,target,True)
    if first_ind==-1:
        print("no occurance:")
    print(f" occurance :{second_ind-first_ind+1}")