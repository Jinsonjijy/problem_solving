"""
Recursive Implementation of atoi()


17

Problem Statement: Implement the function myAtoi(s) which converts the given string s to a 32-bit signed integer (similar to the C/C++ atoi function).

Steps to Implement: 1. First, ignore any leading whitespace characters ' ' until the first non-whitespace character is found.
2. Check the next character to determine the sign. If it’s a '-', the number should be negative. If it’s a '+', the number should be positive. If neither is found, assume the number is positive.
3. Read the digits and convert them into a number. Stop reading once a non-digit character is encountered or the end of the string is reached. Leading zeros should be ignored during conversion.
4. The result should be clamped within the 32-bit signed integer range: [-2147483648, 2147483647]. If the computed number is outside this range, return -2147483648 if the number is less than -2147483648, or return 2147483647 if the number is greater than 2147483647.
5. Finally, return the computed number after applying all the above steps.
"""
def string_to_int(str1):
    str1=str1.lstrip()
    res=0
    n=len(str1)
    sign=1
    if str1[0]=="-":
        sign=-1
    elif str1[0]=="+":
        sign=1

    def backtracking(i):
        nonlocal res
        if not(str1[i].isdigit()):
            return
        if i==len(str1)-1:
            res=res*10+int(str1[i])
            return
        if str1[i].isdigit():
            res=res*10+int(str1[i])
            return backtracking(i+1)
    backtracking(1)
    res*=sign
    if res<-2**31:
        return -2**31
    elif res>2**31 -1 :
        return 2**31 -1
    else:
        return res
print(string_to_int(input()))