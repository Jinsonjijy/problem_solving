"""

Rearrange Array Elements by Sign


15

Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

"""
arr=[1,2,-4,-5]
n=len(arr)
neg_arr=[]
pos_arr=[]
res=[]
for val in arr:
    if val>0:
        pos_arr.append(val)
    else:
        neg_arr.append(val)
for i in range(n//2):
    res.append(pos_arr[i])
    res.append(neg_arr[i])
for val in res:
    print(val,end=" ")
"""
arr = [1,2,-4,-5]
n = len(arr)

res = [0] * n

pos = 0
neg = 1

for val in arr:
    if val > 0:
        res[pos] = val
        pos += 2
    else:
        res[neg] = val
        neg += 2

print(res) this approach is also good

"""
pos=0
neg=1
res1=[0]*n
for val in arr:
    if val>0:
        res1[pos]=val
        pos+=2
    else:
        res1[neg]=val
        neg+=2
print([val for val in res1])