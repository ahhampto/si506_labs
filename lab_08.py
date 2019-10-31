# PROBLEM 1
# In this problem you will demonstrate your understanding of
# 1) working with dictionaries
# 2) working with lists
# 3) manipulating data using dictionaries
# 4) converting the values of dictionaries to lists

# Problem 01 SETUP - We provide you with a dictionary to start the lab problem.

fruits = {'apple': 10, 'banana': 20, 'strawberry': 6, 'orange' : 9}
num_fruits = []

# Problem 01 END SETUP

# BEGIN PROBLEM 1 SOLUTION
# Store the values of the dictionary fruits in the list named 'num_fruits'.
# The desired answer is [10, 20, 6, 9]
# Hint: You can do this by calling the values of the dictionary.

for key, value in fruits.items():
	#print(f'key: {key}', 'value: {value}'')
	num_fruits.append(value)#append value of fruit to num_fruits list
	print(f'num_fruits:{num_fruits}')

print(num_fruits)

#ALTERNATE
#for value in fruits.values():
#	num_list.append(value)

# PROBLEM 2
# In this problem, you will demonstrate your understanding of
# 1) iterating through the dictionary
# 2) adding values
# 3) saving tha value to a variable

# Problem 02 SETUP - We provide you with a variable to start the problem.

sum_fruits = 0

# Problem 02 END SETUP

# BEGIN PROBLEM 2 SOLUTION
# Find the sum of the values of the fruits dictionary. Do not use the list num_fruits.
# Iterate through each key-value pair in the dictionary and add the numbers.
# Save the sum of the numbers to the variable named sum_fruits.

for key in fruits:
	sum_fruits += fruits[key]

print(sum_fruits)

# PROBLEM 3
# In this problem you will demonstrate your understanding of
# 1) working with dictionary
# 2) working with values
# 3) finding the largest value

# Problem 03 SETUP - We provide you with a variable to start the problem.

max_fruits = 0

# Problem 03 END SETUP

# BEGIN PROBLEM 3 SOLUTION
# Find the largest value in the fruits dictionary. Do not use the list num_fruits. Save the largest value to the
# variable named max_fruits.

max_fruits = max(fruits.values())
print(max_fruits)

# PROBLEM 4
# In this problem you will demonstrate your understanding of
# 1) creating a new dictionary using an existing one
# 2) iterating through a dictionary
# 3) working with values
# 4) connecting the keys based on value

# Problem 04 SETUP - We provide you with a variable to start the problem

new_dict = {}

# Problem 04 END SETUP

# BEGIN PROBLEM 4 SOLUTION
# Create a new dictionary using the fruits dictionary. Save the key-value pairs which has a value of
# more than 6 to the new dictionary named 'new_dict'.
# Iterate through the dictionary fruits.
# Use if statement to check if the value is greater than 6.
# Add the pair to the new dictionary.

for key, value in fruits.items():
	if value > 6:
		#print(key, value)
		new_dict.update([('apple', 10), ('banana', 20), ('orange', 9)])

print(new_dict)
