"""


Generate Paranthesis


5

Problem Statement: Given n pairs of parentheses, write a function to generate all combinations of well-formed parenthese


"""
def generate_para(n):
    res=[]
    def backtracking(curr):
        if len(curr)==n:
            res.append(curr.copy())



generate_para(map(int,input().split()))