"""
Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.

NOTE: Elements in the union should be in ascending order

"""
# arr1=list(map(int,input().split(" ")))
# arr2=list(map(int,input().split(" ")))
# dict1={}
# arr3=[]
# for val in arr1:
#     if val in dict1:
#         dict1[val]+=1
#     else:
#         dict1[val]=1
# for val in arr2:
#     if val in dict1:
#         dict1[val]+=1
#     else:
#         dict1[val]=1
# arr3.extend(dict1.keys())
# print(arr3)
#the above one is a optimised code but we can use another approach because the arrays are sorted and use two pointer
# one pointer in one array and another in next array
arr1=list(map(int,input().split(" ")))
arr2=list(map(int,input().split(" ")))
i=0
j=0
union=[]
while i<len(arr1) and j<len(arr2):
    if i>0 and arr1[i]==arr1[i-1]:
        i+=1
        continue
    if j>0 and arr2[j]==arr2[j-1]:
        j+=1
        continue
    elif arr1[i]<arr2[j]:
        union.append(arr1[i])
        i+=1
    elif arr1[i]>arr2[j]:
        union.append(arr2[j])
        j+=1
    else:
        union.append(arr1[i])
        i+=1
        j+=1
while j<len(arr2):
    if j>0 and arr2[j]!=arr2[j-1]:

        union.append(arr2[j])
    j+=1
while i<len(arr1):
    if i>0 and arr1[i]!=arr1[i-1]:
        union.append(arr1[i])
    i+=1
print(union)
#the above one is a valid solution