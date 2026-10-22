"""

185. Find Nth root of a number
Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.

Example 1:
Input: N = 3, M = 27

Output: 3

Explanation: The cube root of 27 is equal to 3.

Example 2:
Input: N = 4, M = 69

Output:-1

Explanation: The 4th root of 69 does not exist. So, the answer is -1.
"""
def find_nth_root(m,n):
    l=0
    r=m

    while l<=r:
        mid=(l+r)//2
        res=mid**n
        if res==m:
            return mid
        elif res>m:
            r=mid-1
        else:
            l=mid+1
    return -1




if __name__=="__main__":
    m=int(input())
    n=int(input())
    print(find_nth_root(m, n))