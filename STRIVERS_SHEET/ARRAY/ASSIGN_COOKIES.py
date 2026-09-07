"""
we have students=>[1,2,3] and this is their need for cookie
also we have cookie set =>[1,1]
output: 1
we need to return the number of student getting the count
"""
if __name__=="__main__":
    student=list(map(int,input().split(" ")))
    cookies=list(map(int,input().split(" ")))
    student.sort()
    cookies.sort()
    count,j,i=0,0,0
    while i<len(student) and j<len(cookies):
        if cookies[j]>=student[i]:
            count+=1
            i+=1
        j+=1
    print(count)