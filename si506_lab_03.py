print('Lab Exercise 03 \n')

We provide you with a select list of UMSI faculty. In the future, such data
# will be provided in a file which you will read into Python with some useful functions. However,
# for today, the teaching team has provided this list for you to use.
#
# Data description:
# Each item in the umsi_faculty list is a string containing the name, title, and email address of
# the faculty member. Each piece of information relating to the faculty member is separated by a
# pipe ('|') delimiter.
umsi_faculty = ["Charles Severance|Clinical Professor of Information|csev@umich.edu",
                "Colleen Van Lent|Lecturer|collemc@umich.edu",
                "Chris Teplovs|Lecturer|cteplovs@umich.edu",
                "Anthony Whyte|Lecturer|arwhyte@umich.edu",
                "Christopher Brooks|Research Assistant Professor|brooksch@umich.edu"]

# PROBLEM 1
# Part I. Extract the second item in umsi_faculty using its index value and assign it to a new
# variable named collemc.
# Part II. Extract the last element in umsi_faculty using its index value and assign it to a new
# the variable named brookcsh.
collemc = umsi_faculty[1]
print(collemc)
brookcsh = umsi_faculty[-1]
print(brookcsh)

# PROBLEM 2
# Use list slicing to extract the 2nd, 3rd and 4th items from the list umsi_faculty and save
# the items to a new list called lecturers.
lecturers = umsi_faculty[1:4]
print(lecturers)

# PROBLEM 3
# There are two parts to this problem:
# Part I. Extract each faculty member's email addresses from the umsi_faculty list and append the
# extracted email address to the list named email_addresses.
# Part II. Using an if statement, check the length of each email address in the list.
# If the length of the email address is greater than ('>') 15 characters, extract the
# email address and append it to a new list called long_email_addresses.
csev_email = umsi_faculty[0].split("|")[2]
print(csev_email)

collemc_email = umsi_faculty[1].split("|")[2]
print(collemc_email)

cteplovs_email = umsi_faculty[2].split("|")[2]
print(cteplovs_email)

arwhyte_email = umsi_faculty[3].split("|")[2]
print(arwhyte_email)

brookcsh_email = umsi_faculty[4].split("|")[2]
print(brookcsh_email)

email_addresses = []
email_addresses.append(csev_email)
email_addresses.append(collemc_email)
email_addresses.append(cteplovs_email)
email_addresses.append(arwhyte_email)
email_addresses.append(brookcsh_email)
print(email_addresses)

long_email_addresses = []
for email in email_addresses:
    if len(email) > 15:
        long_email_addresses.append(email)
print(long_email_addresses)
