"""moving zeros
it can be done using two pointer approach
"""
arr=list(map(int,input("").split(" ")))
# print(arr)
l=0
for r in range(len(arr)):
    if arr[r]!=0:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
print(arr)