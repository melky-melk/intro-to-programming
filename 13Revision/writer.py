def writer(filename, lines):
    # because we have a file name we instantly know we need to have a file open command 
    # because we have fle open we need to have a try
    try:
        # it says to raise an error, so we dont really need to have an except block for this error
        if not isinstance(filename, str) or not isinstance(lines, list):
            raise TypeError

        # open the file in write mode. we create a file instance/object here
        f = open(filename, "w")
        
        # loop through the lines, to write them into the file
        i = 0
        while i < len(lines):
            line = lines[i]
            # check if every line inside lines is a string
            if not isinstance(line, str):
                raise ValueError("Cannot write non-string value to file.")

            # to write into the file
            f.write(line + '\n')

            i += 1

        # must close the file at the end PLEASE REMEMBER ITS EASY MARKS 
        f.close()
    except FileNotFoundError:
        print("Cannot find file")

