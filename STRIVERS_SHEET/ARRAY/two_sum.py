arr=list(map(int,input().split(" ")))
k=int(input(""))
hash1={}
for i,val in enumerate(arr):
    if k-val in hash1:
        print(hash1[k-val],val)
        break
    else:
        hash1[val]=i 