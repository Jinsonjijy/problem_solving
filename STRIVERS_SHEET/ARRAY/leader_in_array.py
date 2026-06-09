"""

Leaders in an Array


16

Problem Statement: .

Examples
Example 1:
Input:
 arr = [4, 7, 1, 0]
Output:
 7 1 0
Explanation:
 The rightmost element (0) is always a leader.
7 and 1 are greater than the elements to their right, making them leaders as well.

Example 2:
Input:
 arr = [10, 22, 12, 3, 0, 6]
Output:
 22 12 6
Explanation:
 6 is a leader because there are no elements after it.
12 is greater than all the elements to its right (3, 0, 6), and 22 is greater than 12, 3, 0, 6, making them leaders as well
"""
arr = [10, 22, 12, 3, 0, 6]
res=[]
n=len(arr)
larget=0
second=0
res=[]
res.append(arr[n-1])
for i in range(n-2,-1,-1):
    if arr[i]>max(arr[i+1:]):
        res.append(arr[i])
    else:
        continue
print(res)
"""
the solution is O(n)
arr = [10, 22, 12, 3, 0, 6]

n = len(arr)

max_right = arr[-1]
res = [max_right]

for i in range(n - 2, -1, -1):
    if arr[i] > max_right:
        res.append(arr[i])
        max_right = arr[i]

res.reverse()
print(res) this is the optimal solution

"""