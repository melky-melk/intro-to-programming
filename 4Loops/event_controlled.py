# we want to make a secret password that keeps asking for input until it gets the right oct

# lets first save our input into a variable
password = input("What is the password? ")

while (password != "secret"):
    password = input("Incorrect password try again: ")

print("Hello Chiara")
