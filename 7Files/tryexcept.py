user_input = input("Enter a number: ")

try: # tries to do this...
    n = int(user_input)
    x = n + 5
    print(x)
except ValueError: # if there's a ValueError, do this instead
    print("That's not a number!")

# n = int(user_input)
# x = n + 5
# print(x)
