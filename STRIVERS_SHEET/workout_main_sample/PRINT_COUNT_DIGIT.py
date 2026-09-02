if __name__=="__main__":
    str1=input()
    dict1={'0':0,'1':0,'2':0,'3':0}
    for dig  in str1:
        if dig.isdigit():
            if dig not in dict1:
                dict1[dig]=1
            else:
                dict1[dig]+=1
    res=""
    for val in sorted(dict1.keys()):
        res.join(str(dict1[val]))
    print(res)
