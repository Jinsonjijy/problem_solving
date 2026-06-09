"""
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.
"""
arr=[0,1,2,1,0,0,1,1,2,2,0,0]
hash_tab={}
res=[]
for val in arr:
    if val not in hash_tab:
        hash_tab[val]=1
    else:
        hash_tab[val]+=1
for val in hash_tab:
    res+=[val]*hash_tab[val]
print(res)