filepath = "anotherfolder/stuff.txt"
# open(file path, mode)
f = open(filepath, 'r')
# reads one line
line = f.readline()
print(line)
f.close()

