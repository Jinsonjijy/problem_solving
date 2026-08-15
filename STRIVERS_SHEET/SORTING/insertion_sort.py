""""
lets create a insertion sort algorithm

watched the leetcode insertion sort algorithm
"""
def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i-1
        while (j>=0 and arr[j+1]<arr[j]):
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
            j=j-1
arr=list(map(int,input().split(" ")))
insertion_sort(arr)
print(*arr,sep="->")