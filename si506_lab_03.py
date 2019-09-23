print('Lab Exercise 03 \n')
umsi_faculty = ["Charles Severance|Clinical Professor of Information|csev@umich.edu",
                "Colleen Van Lent|Lecturer|collemc@umich.edu",
                "Chris Teplovs|Lecturer|cteplovs@umich.edu",
                "Anthony Whyte|Lecturer|arwhyte@umich.edu",
                "Christopher Brooks|Research Assistant Professor|brooksch@umich.edu"]

# PROBLEM 1
collemc = umsi_faculty[1]
print(collemc)
brookcsh = umsi_faculty[-1]
print(brookcsh)

# PROBLEM 2
lecturers = umsi_faculty[1:4]
print(lecturers)

# PROBLEM 3
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
