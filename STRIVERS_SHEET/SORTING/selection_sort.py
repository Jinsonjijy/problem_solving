"""
this is basic implementation of selection sort algorithm
    in this we need to make sure on left max values are appended each time
     the time complexity=>O(n^2)
     the space compelxity=>O(n)
"""
def selection_sort(arr):
    smallest=0
    for i in range(len(arr)):
        smallest=min(arr[i:])
        arr.remove(smallest)
        arr.insert(0,smallest)
    return arr[::-1]
if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    print(selection_sort(arr))
