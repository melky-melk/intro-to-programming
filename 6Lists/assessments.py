# replace the ... with the rest of the strings!
# assessments = ["Participation: 8%", ...]

# it wants us to have all of our string sin a list, and then print them out using a while loop

# make a list of the strings that we need
ls = ["Participation: 8%", "Small Test: 20%", "Assignment: 30%", "Online task: 12%", "Exam: 30%"]

# we want to print out all of these things in a loop

i = 0
# want to make it so that i keeps incrementing until we hit the end of our list
while (i < 5):
    print(ls[i])
    # next we want to increment i so it goes to the next element in the list
    i += 1

