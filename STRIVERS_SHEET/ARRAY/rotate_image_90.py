"""
Rotate Image by 90 degree




Problem Statement: Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise. The rotation must be done in place, meaning the input 2D matrix must be modified directly
"""
matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
n=len(matrix)# this rotation of the matrix only happens in the the square matrix
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
# we have done the transponse the matrix
for val in matrix:
    val.reverse()
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end="  ")
    print("\n")
