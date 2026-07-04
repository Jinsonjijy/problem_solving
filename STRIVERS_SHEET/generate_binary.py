"""

Generate all binary strings


13

Problem Statement: Given an integer n, return all binary strings of length n that do not contain consecutive 1s. Return the result in lexicographically increasing order.

A binary string is a string consisting only of characters '0' and '1'.

Examples
Example 1:
Input:
 n = 3
Output:
 ["000", "001", "010", "100", "101"]
Explanation:
 All binary strings of length 3 that do not contain consecutive 1s.

Example 2:
Input:
 n = 2
Output:
 ["00", "01", "10"]
Explanation:
 All binary strings of length 2 that do not contain consecutive 1s.
"""
def generatring(n):
    res=[]
    def backtracking(curr,prev):
        if len(curr)==n:
            res.append(curr[:])
            return
        backtracking(curr+"0","0")
        if prev!="1":
            backtracking(curr+"1","1")
    backtracking("","")
    return res

n=int(input())
print(generatring(n))