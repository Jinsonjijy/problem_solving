"""
in this we need to find the missing number from a range of aray

"""
# arr=list(map(int,input().split(", ")))
# n=len(arr)
# hash=[0]*(n+1)
# for i in range(1,len(arr)):
#     hash[arr[i]]=1
# for i in range(1,len(hash)):
#     if hash[i]==0:
#         print(i)
#         break
# another approach is simple take the sum using n natural number and then subtract from the
arr=list(map(int,input().split(", ")))
n=len(arr)+1
exp_sum=n*(n+1)//2
got_sum=sum(arr)
print(exp_sum-got_sum)