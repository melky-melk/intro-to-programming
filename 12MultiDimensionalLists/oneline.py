def unjagged_list(jagged_list):
    # loops through jagged #takes the inner list and loops through all of the lists again to find the minimum value then cuts the inner list to that size
    for i in range(len(jagged_list)): jagged_list[i] = jagged_list[i][:min([len(row) for row in jagged_list])]

def swap(matrix, i, j):
    matrix[i], matrix[j] = (matrix[i], matrix[j]) if max(matrix[min(i, j)]) < max(matrix[max(i, j)]) else (matrix[j], matrix[i])



