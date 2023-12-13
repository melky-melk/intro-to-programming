# break is a way to exit the loop without changing teh original condition
# once the break command is run the loop will be exited immediately without reading all the other lines


i = 0
while (i < 10):
    print(i)
    if i == 7:
        # this will exit the loop before reading off any of the other lines
        break
    i += 1


while True:
    print("something")
    break
    # this line will never print since the loop is exited before this line can be read
    print("another thing")
