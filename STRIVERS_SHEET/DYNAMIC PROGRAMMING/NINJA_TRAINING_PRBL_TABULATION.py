"""
Ninja's Training
58 mins read
The Jat
Easy
Updated 1 year ago
Dynamic  Programming
Problem Statement
A ninja has planned a n-day training schedule. Each day he has to perform one of three activities - running, stealth training, or fighting practice. The same activity cannot be done on two consecutive days and the ninja earns a specific number of merit points, based on the activity and the given day.Programming

Given a n x 3-sized matrix, where matrix[i][0], matrix[i][1], and matrix[i][2], represent the merit points associated with running, stealth and fighting practice, on the (i+1)th day respectively. Return the maximum possible merit points that the ninja can earn.

Examples
plaintext
Copy
Example 1:

Input: matrix = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
Output: 210

Explanation:
Day 1: fighting practice = 70
Day 2: stealth training = 50
Day 3: fighting practice = 90
Total = 70 + 50 + 90 = 210
This gives the optimal points.
plaintext
Copy
Example 2:

Input: matrix = [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
Output: 290

Explanation:
Day 1: running = 70
Day 2: stealth training = 20
Day 3: running = 200
Total = 70 + 20 + 200 = 290
This gives the optimal points.
over commed the overlapping subproblem


"""
if __name__=="__main__":
    arr=[]
    day=int(input("enter the number of days"))
    for i in range(day):
        row=list(map(int,input().split(" ")))
        arr.append(row)
        row=[]
    dp=[[0]*4 for _ in range(day)]#so this create a specific array ok so not [[0]*4]*day it creat same referenced list inside the list
    print(dp)
    print(*arr,sep="\n")
    dp[0][0]=max(arr[0][1],arr[0][2])
    dp[0][1]=max(arr[0][0],arr[0][2])
    dp[0][2]=max(arr[0][0],arr[0][1])
    dp[0][3]=max(arr[0][0],max(arr[0][1],arr[0][2]))

    for day in range(1,len(arr)):
        for last in range(4):#here the prev activity 0,1,2 and 3 if no acitivity
            maxi=0
            for task in range(3):
                if task!=last:
                    activity=arr[day][task]+dp[day-1][task]
                    maxi=max(activity,maxi)
            dp[day][last]=maxi
    print(dp[len(arr)-1][3])