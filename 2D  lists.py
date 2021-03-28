
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# matrix[0][1] = 20 (can change the value)
print (matrix[0][0]) # first line and first number
print (matrix[0][1]) # first line and second number

for row in matrix:
    for item in row:
        print(item)