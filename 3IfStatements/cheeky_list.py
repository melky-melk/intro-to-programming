# you can stoire multiple variables of something inside a list
# a list is a variable that is able to hold multiple variables
valid_stations = ["A", "B", "C"]

start = "D"

# python has a built in function called in, for lists, so you can check whether
# your variable, start, is in something
# but since we want to check if something is invalid, we will use the not keyword
# so that if the start is not in the valid stations it will return True
# therefore activating the if statement condition 
if not start in valid_stations:
    print("this station is invalid")

