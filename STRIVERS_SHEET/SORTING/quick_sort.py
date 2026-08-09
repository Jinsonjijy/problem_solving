
# ""
# this is just a doct string
# "" this is not a quick_sort it is just a bubble sort algorithm
def quick_sort(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))
print(quick_sort(arr))