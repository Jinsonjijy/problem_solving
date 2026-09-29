"""
implementation of valid parathesis problem question leetcode
"""
def valid_para(s):
    stack=[]#lifo
    mapping={")":"(","}":"{","]":"[",">":"<"}
    for char in s:
        if char in mapping:
            if stack and stack[-1]==mapping[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False
if __name__=="__main__":
    s=input("")
    print(valid_para(s))
