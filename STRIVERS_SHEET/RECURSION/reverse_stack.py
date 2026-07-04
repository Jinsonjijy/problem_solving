"""
reversing stack using the recursion
"""
def reverse_stack(stack,i,r):
    if i>=r:
        return
    stack[i],stack[r]=stack[r],stack[i]
    reverse_stack(stack,i+1,r-1)
arr=list(map(int,input().split()))
reverse_stack(arr,0,len(arr)-1)
print(arr)