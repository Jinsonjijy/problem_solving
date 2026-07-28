"""

Question 4: Employee Management — Insert in Sorted Order (Asked:
2023)
Problem Statement:
An Employee Management System stores employee details sorted by employee ID in
ascending order. Given a list of existing employee IDs and a new employee ID, insert the new
ID at the correct position to maintain sorted order. Print the updated list.
Input Format: - First line: integer N (number of existing employees) - Second line: N space
separated integers (sorted employee IDs) - Third line: integer newID
Output Format: - Updated sorted list
Example:
Input:
5
101 103 105 107 109
104
Output:
101 103 104 105 107 109

"""
flag=0
no_employees=int(input())
employess=list(map(int,input().split(" ")))
new=int(input())
for ind,employe in enumerate(employess):
    if new<=employe:
        employess.insert(ind,new)
        flag=0
        break
    else:

        flag=1

if flag==1:
    employess.append(new)
print(*employess,sep=",")