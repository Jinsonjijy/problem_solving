
"""

Track
Command Palette
Search for a command to run...

Blog
Discussion
Sort a Stack


10

Problem Statement: You are given a stack of integers. Your task is to sort the stack in descending order using recursion, such that the top of the stack contains the greatest element. You are not allowed to use any loop-based sorting methods (e.g., quicksort, mergesort). You may only use recursive operations and the standard stack operations (push, pop, peek/top, and isEmpty).
"""
def insert_stack(stack,x):
    if not stack or stack[-1]<=x:
        stack.append(x)
        return
    temp=stack.pop()
    insert_stack(stack,x)
    stack.append(temp)
def sort_stack(stack):
    #base condition
    if len(stack)<=1:
        return
    temp=stack.pop()
    sort_stack(stack)
    insert_stack(stack,temp)

arr=list(map(int,input().split()))
sort_stack(arr)
print(arr)
