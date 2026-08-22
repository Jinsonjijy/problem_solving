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
def training(arr):
    dp=[[-1]*4]*len(arr)
    def backtracking(day,last):
        if day ==0:
            maxi=0
            for task in range(0,3):
                if task!=last:
                    point=arr[0][task]
                    maxi=max(point,maxi)
            return maxi
        maxi=0
        if dp[day][last]!=-1:
            return dp[day][last]
        for task in range(3):
            if task!=last:
                point=arr[day][task]+backtracking(day-1,task)
                maxi=max(point,maxi)
        dp[day][last]=maxi
        return dp[day][last]#always store in the dependent indexes
    return backtracking(len(arr)-1,3)



day=int(input("enter the day"))
arr=[]
for i in range(day):
    row=[]
    for j in range(3):
        row.append(int(input()))
    arr.append(row)
print(*arr,sep="\n")
print(training(arr))
