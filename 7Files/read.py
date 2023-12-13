# Write a program which prints out N lines from a given file. 
# Both the filename and value  N will be provided as command line arguments - eg:

# first we want to read from our command line arguements
import sys

try:
    # index error
    filename = sys.argv[1]
    num_of_lines = sys.argv[2]
    
    # value error
    num_of_lines = int(sys.argv[2])

    # file not found error
    f = open(filename, "r")

    i = 0
    lines = []
    while (i < num_of_lines):
        # read the current line we are at then remove the whitespace
        line = f.readline()

        if line == "":
            break
        
        print(line, end="")
        i += 1

    f.close()
# it can deal with both errors simulteneously, both the file not found and the value
except FileNotFoundError:
    print(f"Error: unable to open {filename}")
except ValueError:
    print(f"Error: invalid number {num_of_lines}")
except IndexError:
    print("Error: not enough arguments")
