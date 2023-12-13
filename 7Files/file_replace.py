filename = "vhdsgf"
f = None

try:
    f = open(filename)
except FileNotFoundError:
    f = open("sample.txt")

