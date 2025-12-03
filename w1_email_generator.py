import sys
import random
import pyperclip

def gmail():
    print("You have chosen Gmail!")
    print("I need the following details to create your Gmail email address...")
    Fname = input("Please enter your first name: ")
    Fname = Fname.lower()
    while not Fname.isalpha():
        print("Invalid input: Numericals (0-9), spaces, punctuation (.;@) Forbidden.")
        Fname = input("Ree-enter your first name: ")
        Fname = Fname.lower()
    Sname = input("Please enter your last name: ")
    Sname = Sname.lower()
    while not Sname.isalpha():
        print("Invalid input: Numericals (0-9), spaces, punctuation (.;@) Forbidden.")
        Sname = input("Ree-enter your last name: ")
    email = Fname[0:3] + Sname[0:3] + str(random.randint(0,9))+ str(random.randint(0,9))+ str(random.randint(0,9)) + "@gmail.com"
    print("Your generated email address: " + email)
    print("This email has now been saved to your clipboard.")
    pyperclip.copy(email)

def outlook():
    print("You have chosen Outlook!")
    print("I need the following details to create your Outlook email address...")
    Fname = input("Please enter your first name: ")
    Fname = Fname.lower()
    while not Fname.isalpha():
        print("Invalid input: Numericals (0-9), spaces, punctuation (.;@) Forbidden.")
        Fname = input("Ree-enter your first name: ")
        Fname = Fname.lower()
    Sname = input("Please enter your last name: ")
    Sname = Sname.lower()
    while not Sname.isalpha():
        print("Invalid input: Numericals (0-9), spaces, punctuation (.;@) Forbidden.")
        Sname = input("Ree-enter your last name: ")
        name = Fname.lower()
    email = Fname[0:3] + Sname[0:3] + str(random.randint(0,9))+ str(random.randint(0,9))+ str(random.randint(0,9)) + "@outlook.com"
    print("Your generated email address: " + email)
    print("This email has now been saved to your clipboard.")
    pyperclip.copy(email)
    
def yahoo():
    print("You have chosen Yahoo!")
    print("I need the following details to create your Yahoo email address...")
    Fname = input("Please enter your first name: ")
    Fname = Fname.lower()
    while not Fname.isalpha():
        print("Invalid input: Numericals (0-9), spaces, punctuation (.;@) Forbidden.")
        Fname = input("Ree-enter your first name: ")
        Fname = Fname.lower()
    Sname = input("Please enter your last name: ")
    Sname = Sname.lower()
    while not Sname.isalpha():
        print("Invalid input: Numericals (0-9), spaces, punctuation (.;@) Forbidden.")
        Sname = input("Ree-enter your last name: ")
        name = Fname.lower()
    email = Fname[0:3] + Sname[0:3] + str(random.randint(0,9))+ str(random.randint(0,9))+ str(random.randint(0,9)) + "@yahoo.com"
    print("Your generated email address: " + email)
    print("This email has now been saved to your clipboard.")
    pyperclip.copy(email)
    


print("Hello there!")
print("Welcome to the email generator.")
email_choice = input("Please select from the following options: Gmail [1] Outlook [2] Yahoo [3]: ")
while email_choice not in ('1','2','3'):
    print("Invalid input.")
    email_choice = input("Please select from the following options: Gmail [1] Outlook [2] Yahoo [3]: ")
if email_choice == '1':
    gmail()
    print("Service terminated.")
    sys.exit()
if email_choice == '2':
    outlook()
    print("Service terminated.")
    sys.exit()
if email_choice == '3':
    yahoo()
    print("Service terminated.")
    sys.exit()
while email_choice not in ('1','2','3'):
    print("Invalid input.")
    email_choice

