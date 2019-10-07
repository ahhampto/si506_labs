# In this lab, we use txt files. Be very careful that a line in txt files
# should contain a new line "\n" character at the end of this line.

# PROBLEM 1
# Define a function named "concatenate_name_type".
# The function accepts two arguments - one is "file_name", the other is "file_type". Both two arguments are strings.
# For given arguments, the function should return "<file_name>.<file_type>"
# Pass two defined variables "file_name", "file_type" to the function, assign the result to "full_file_name"
# Print "full_file_name".

f_name = "file1"
f_type = "txt"
full_file_name = None

def concatenate_name_type(file_name, file_type):
    return f"{file_name}.{file_type}"

full_file_name = concatenate_name_type(f_name, f_type)

print(full_file_name)

# PROBLEM 2
# 2a) Define a function named "write_into_file"
# The function accepts two arguments - one is "filename", the other is "file_content"
# "filename" is a string and "file_content" is a list of strings
#
# 2b) Open the file with "full_file_name"
#       1) read all lines,
#       2) store the last two lines into the variable "last_two_lines"
# Make sure that there is a new line character "\n" at the end of each line in "last_two_lines"
# Write "last_two_lines" into a new file called "file2.txt" using the function "write_into_file"
# Print "last_two_lines"

def write_into_file(filename, file_content):
    # write the variable <file_content> into the file <filename>
    file_handle = open(filename, 'w') #opened filename to write
    for line in file_content:
        file_handle.write(line) #writing variable into file
        #write/writelines similar to read/readlines...doing actions to single/multiple
    file_handle.close()
    #this doesn't need a return

#write_into_file("file5.txt", ["test\n", "lines\n"]) #testing

last_two_lines = []

file_handle_in = open("file1.txt", "r")
all_lines = file_handle_in.readlines()
last_two_lines = all_lines[-2:]
write_into_file("file2.txt", last_two_lines)
file_handle_in.close()

print(last_two_lines)

# PROBLEM 3
# Finally, put all you've learned together.
# 1) Open each file with file_name in "file_name_list" and "file_type",
#       1) read all lines and
#       2) store those unique lines into the variable "unique_lines".
# NOTE: Make sure that there is a new line character "\n" at the end of each line in "unique_lines".
# 2) Write "unique_lines" into a new file called "summary.txt" using the function "write_into_file".
# 3) Print "unique_lines".

file_name_list = ["file1", "file2", "file3"]
file_type = "txt"
unique_lines = []

for file_name in file_name_list:
    full_file_name = concatenate_name_type(file_name, file_type)
    file_handle = open(full_file_name, 'r')
    all_lines = file_handle.readlines()
    for line in all_lines:
        if line not in unique_lines:
            unique_lines.append(line)
    file_handle.close()

write_into_file("summary.txt", unique_lines)
print(unique_lines)
