#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

    
# Open the file and read the contents
sample_file = open("textfile.txt", "r")


    # use the read() function to read the entire file
if sample_file.mode == 'r':
#     //contents = sample_file.read()
# //    print(contents)
    files_lines = sample_file.readlines()
    for line in files_lines:
        print(line)