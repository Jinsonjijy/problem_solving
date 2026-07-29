def func_calling():
    print(f"name of the calling function",{__name__})
def add(a,b):
    return a+b
def binnary_search(arr,target):
    l=0
    r=len(arr)
    while l<r:
        mid=(l+r)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            l+=1
        elif arr[mid]>target:
            r-=1
    return -1

if __name__=="__main__":# mainly for modularity and for working with modules
    print(f"name of function ",{__name__})
    func_calling()  # their is specail keywords or names are generated while making the funciton it is called dunder for python
    func_calling()
    print(add(2, 3))