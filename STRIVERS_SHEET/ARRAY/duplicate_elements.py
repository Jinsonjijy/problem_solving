"""Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements."""


"""k=input()
arr=[int(x) for x in k.split(" ")]"""
# here this is the way we can just take from the split function
k=input("")
arr=list(map(int,k.split(" ")))
# print(arr)
value=True
for i in range(len(arr)-1):
    if arr[i]==arr[i+1]:
        print("duplicates found")
        break
    else:
        value=False
print("duplicated is ",value)
