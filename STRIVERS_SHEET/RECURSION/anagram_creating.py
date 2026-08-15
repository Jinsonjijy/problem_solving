from collections import Counter
def anagram_creating(name):
    dict_name=dict(Counter(name))
    print(dict_name)
    res=[]
    def backtracking(v):
        if len(v)>=3:
            res.append(""+str(v.copy()))
            return
        for val in sorted(dict_name):
            if dict_name[val]>=1:
                v.append(val)
                backtracking(v)
                v.pop()
                backtracking(v)
    backtracking([])
    return res



if __name__=="__main__":
    name=input("enter the name:")
    anagram_creating(name)