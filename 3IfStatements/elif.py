# say we wanted to see what certain numbers are divisible by

# first we take a value and then save it into this variable
value = int(input("please input a number: "))

# lets check if it is divisible by 2
if value % 2 == 0:
    print("this statement is divisible by 2")
# when if is used each individual statement will checked on its own
# when elif is used the if statement is checked, and if that is true, it will ignore all elif
if value % 3 == 0:
    print("this statement is divisible by 3")
if value % 1 == 0:
    print("this statement is divisible by 1")

