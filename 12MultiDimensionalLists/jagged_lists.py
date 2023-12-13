# Write your code here

def traverse(ls):
    # this list has inner lists as its elements 
    i = 0
    while i < len(ls):
        inner_ls = ls[i]
        
        #while we have the inner list saved, we can loop through those values by going through that length 
        j = 0
        while j < len(inner_ls):
            print(inner_ls[j], end = " ") # want to end on spaces and not new lines
            j += 1
        # when we finish looping through the values of the inner list we add a new line 
        print()

        i += 1


ls_a = [[1, 2], [3, 4, 5, 6], [7, 8, 9]]  # 3 "rows", each row has a different length

traverse(ls_a)  # prints:
