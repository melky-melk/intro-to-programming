def my_or(a, b):
    return not (not a and not b) # a or b

def my_or2(a, b):
    if a:
        return True
    if b:
        return True
    # if neither of those values have returned yet then that means both values were false so we can return false
    return False

def my_or3(a, b):
    # the integer value for true is 1, the value for false is 0
    # if you add them together you are able to determine whether or not you have any of the variables as true
    # anything above 0 is considered true
    return bool(int(a) + int(b))

print(my_or(False, False))
print(my_or(True, False))
print(my_or(True, True))
