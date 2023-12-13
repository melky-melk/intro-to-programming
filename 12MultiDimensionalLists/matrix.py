matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]  # call this matrix `A`

# this will go by the columns. it will stay on the column 1 and iterate through the rows
# before going to column 2 and iterating through the rows
for j in range(2):
    # this goes through rows of the matrix
    for i in range(3):
        print(matrix[i][j], end=' ')
    print()

#i =  0   1   2
#j = 01  01  01
#    12  34  56

#j =  0   1 
#i = 012 012
#    135 246

"""
How could the above loop structure be modified, to print the transpose?
The transpose of the above matrix `A` is:
1 3 5
2 4 6
"""

