# there are 2 main ways i use to get rid of a comma at the end
# broken into get_rid_of_comma_1 and get_rid_of_comma_2 
num = 1
line = ''

while (num <= 100):
    # the first method is to use an if statement to check whether we are at the last variable
    # then if we are, add to the string without the comma
    if num == 99:
        line += '99'
    # we should use an elif here, so that when we check if it is 99, it will ignore everything else and not check if it is odd
    # therefore, it will never append to the line this additional 99 with the comma
    elif num % 2 != 0:
        line += str(num) + ', '
    num += 1
print(line)

