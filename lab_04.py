print('Lab Exercise 04 \n')

# Data description
# Problem 3 will involve working with the list of integers named numbers.
numbers = [1, 2, 3, 4, 5, 6]

# PROBLEM 1
# Define a function named multiply. The function accepts two arguments, both integers,
# For this problem, pass to the function the integers 506 and 507, multiply them together,
# and return the result.

def multiply(class_1, class_2):
    return class_1*class_2

print(multiply(506, 507))

# PROBLEM 2 (10 Points)
# Define a function named greeting. The function accepts a string value and adds the value to
# a string comprising the greeting, i.e., "How are you doing <name>?
# For this problem the value to pass to the function is "Rob".

def greeting(name):
    return ''.join(["How are you doing ", name, "?"])

print(greeting('Rob'))

# PROBLEM 3 (10 Points)
# Define a function named sum_all. The function accepts a list of integers named numbers as an argument.
# Call the function passing it numbers and iterate over the list, returning the sum of the integers in the list.

# BEGIN PROBLEM 3 SOLUTION

def sum_all(numbers):
    return sum(numbers)

print(sum_all(numbers))
