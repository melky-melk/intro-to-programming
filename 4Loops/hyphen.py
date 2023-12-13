'''
input: spell output: s-p-e-l-l
input: me output: m-e
'''

# we want to input something and then output the same thing with hyphens

# first we will take our input and setup our final output
string = input()
output = ""

i = 0
while (i < len(string) - 1):
    # we take whatever character we are current at and add it to our output plus the -
    output += string[i] + "-"
    # then we want to move to the next character
    i += 1
output += string[i]
print(output)

