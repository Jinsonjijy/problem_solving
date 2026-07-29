import file1
print(file1.add(4,5))
file1.func_calling()
# this functionality is mainly used in the case of modules this help in unit testing and pytesting
if __name__=="__main__":
    arr=list(map(int,input().split()))
    target=int(input())
    print(*arr,sep="->")
    print(file1.binnary_search(arr,target))