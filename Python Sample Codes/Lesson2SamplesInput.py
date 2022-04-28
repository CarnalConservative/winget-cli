"""
File: teach02_sample.py
Author: Brother Burton

Purpose: Practice formatting strings.
"""

print("Please enter the following information:")

# This prints a blank line
print()

first = input("First name: ")
last = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")

# This time I used a \n to make a blank line before this:
print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{last.upper()}, {first.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print("----------------------------------------")


"""
File: teach02_stretch_sample.py
Author: Brother Burton

Purpose: Practice formatting strings.

This program also contains a way to implement the stretch challenges.
"""

print("Please enter the following information:")

print()

# Ask for the basic information
first = input("First name: ")
last = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")

# Ask for the additional information
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month = input("Starting Month: ")
training = input("Completed additional training? ")

# Now print out the ID Card
print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{last.upper()}, {first.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print()

# There are various ways to accomplish the spacing

# In this approach, I told it that hair_color will take exactly 15
# spaces, and month will take 14. That way, the next columns will
# line up. I had to do month 14 (instead of 15) because the word
# 'Month' that came before my value was one letter longer.

print(f"Hair: {hair_color:15} Eyes: {eye_color}")
print(f"Month: {month:14} Training: {training}")
print("----------------------------------------")