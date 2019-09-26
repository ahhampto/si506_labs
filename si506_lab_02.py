print('Lab Exercise 02 \n')

# PROBLEM 01A (25 points)
# Uncomment the variable name and assigned value that adheres to the styling
# convention described in PEP 08 for function and variable names
# (see https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)
# Choose wisely or you will trigger a syntax error.
course_name = 'SI 506'

# Next, append the text ": Programming I" to the value of the variable
# selected above using the appropriate operator. Write code on next line.
course_name = 'SI 506' + ': Programming I'

# Next write a print() statement that prints the variable value to the
# screen. Write code on next line.
print(course_name)

# Next determine the number of characters of your new string value using
# the appropriate builtin function. Assign the value to the variable
# num_chars (replace default value of 0):
#print(len(full_course_name))
num_chars = 21
print(''.join(['num_chars = ', str(num_chars), '\n']))

#ALTERNATE:
#print('Lab Exercise 02 \n')
#course_number = 'SI 506'
#course_name = ': Programming I'
#full_course_name = course_number + course_name
#print(full_course_name)
##print(len(full_course_name))
#num_chars = 21
#print(''.join(['num_chars = ', str(num_chars), '\n']))
