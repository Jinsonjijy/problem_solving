
"""
this is the basic implementation 
of bucket sort algorithm
it work well

         time complexity is =>O(n^2)
         space complexity is =>O(n+m+n) because it is using 3 array
"""

def bucket_sorting(arr):
    last_element=max(arr)
    res=[]
    bucket_arr=[0]*(last_element+1)
    for val in arr:
        bucket_arr[val]+=1

    for i in range(len(bucket_arr)):
        while bucket_arr[i]!=0:
            res.append(i)
            bucket_arr[i]-=1
    
    return res   
arr=list(map(int,input().split()))
print(bucket_sorting(arr))