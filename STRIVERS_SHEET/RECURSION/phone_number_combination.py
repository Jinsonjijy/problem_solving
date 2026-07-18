"""

Track
Command Palette
Search for a command to run...

Blog
Discussion
Letter Combinations of a Phone number


1

Problem Statement: Given a string consisting of digits from 2 to 9 (inclusive). Return all possible letter combinations that the number can represent.

Examples
Example 1:
Input:
 digits = "34"
Output:
 [ "dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi" ]
Explanation:
The 3 is mapped with "def" and 4 is mapped with "ghi".
So all possible combinations by replacing the digits with characters are shown in the output.

Example 2:
Input:
 digits = "3"
Output:
 [ "d", "e", "f" ]
Explanation:
The 3 is mapped with "def"


"""
def combination(ph_no):
    combo = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    res=[]
    def backtracking(i,v,arr,n):
        if len(v)==len(ph_no):
            res.append("".join(v))
            return
        for val in combo[arr[i]]:
            v.append(val)
            backtracking(i+1,v,arr,n)
            v.pop()
    backtracking(0,[],ph_no,len(ph_no))
    return res
phone_number=input("enter the phone number:")
print(combination(phone_number))