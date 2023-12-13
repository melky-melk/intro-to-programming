# we want to return the inner most list
def super_nest(ls):
    #check if the inner ls is currently a type list
    while (type(ls[0]) == list):
        #if it is, then we want to go deeper into the list
        ls = ls[0]
    
    #the condition is broken, when our list has no internal list inside
    return ls

# print(super_nest([[[[1,2,3]]]]))

def super_nest_recursive(ls):
    #base case
    # if the list we currently have has no list inside of it then we return because its not nested
    if (type(ls[0]) != list):
        return ls

    #recursive case
    # otherwise, if it has not returned anything, we want to search again, taking that new inner list as our parameter
    # we want to include this return statement, because this return statement will allow for the previous calls to return what the inner one is
    return super_nest_recursive(ls[0])

print("result: " + str(super_nest_recursive([[[[1,2,3]]]])))

