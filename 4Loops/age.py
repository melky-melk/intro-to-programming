# initialise our variable to true
valid = True
# since this is true, we will eneter our loop
while valid:
    # take the input and convert it to an integer
    age = int(input("What is your age? "))
    
    # if our integer is an unreasonable number, then we change our control variable to false, thus exiting the loop on our next go around
    if age > 0 and age < 200:
        valid = False
    else:
        # otherwise valid remain True!
        print("Please put in a reasonable age, you dummy!\n")
        
print("Your age is: {}".format((age)))
