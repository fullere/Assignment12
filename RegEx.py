# Elizabeth Fuller
# 4/23/20
# RegEx

import re
# methods to look for specific criteria
def check_q(string):
    # looks to see if string has a 'q'
    x = re.search('q', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_the(string):
    # looks to see if string has 'the'
    x = re.search('the', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_ast(string):
    # looks to see if string has a '*'
    x = re.search('\*', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_digit(string):
    # looks to see if string has a digit
    x = re.search('\d', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_period(string):
    # looks to see if string has a '.'
    x = re.search('\.', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_consec_vowel(string):
    # looks to see if string has 2 consecutive vowels
    x = re.findall('[aeiou]{2}', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_space(string):
    # looks to see if string has any whitespaces
    x = re.search('\s', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_triple(string):
    # looks to see if string has any letters that repeat 3 times
    x = re.findall('\w{3}', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_Hello(string):
    # looks to see if string has 'Hello'
    x = re.search('Hello', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_email(string):
    # looks to see if string has an email
    x = re.findall('\w+@\w+\.\w+', string)
    if (x):
        found = True
    else:
        found = False
    return found

# gets user input for string
print("Enter string here:")
string = input("> ")
# creates loop for menu
# menu has the 10 thing to look for and a way to stop the loop
finish = False
while finish is not True:
    print("""What would you like to do?
    Check for 'q' [1]
    Check for 'the' [2]
    Check for '*' [3]
    Check for a digit [4]
    Check for period [5]
    Check for 2 consecutive vowels [6]
    Check for white space [7]
    Check for letters that repeat three times [8]
    Check for 'Hello' [9]
    Check for email [10]
    Exit [11]""")
# get user input for choice, remove any whitespaces
    choice = input("> ")
    choice = choice.strip()
    # call method for chosen search, give output based on if it is found
    if choice == '1':
        # search for 'q'
        find = check_q(string)
        if find is True:
            print(find)
            print("There is a 'q' in the string.")
        else:
            print(find)
            print("There is not a 'q' in the string.")
    elif choice == '2':
        # search for 'the'
        find = check_the(string)
        if find is True:
            print(find)
            print("There is a 'the' in the string.")
        else:
            print(find)
            print("There is not a 'the' in the string.")
    elif choice == '3':
        # search for '*'
        find = check_ast(string)
        if find is True:
            print(find)
            print("There is a '*' in the string.")
        else:
            print(find)
            print("There is not a '*' in the string.")
    elif choice == '4':
        # search for a digit
        find= check_digit(string)
        if find is True:
            print(find)
            print("There is a digit in the string.")
        else:
            print(find)
            print("There is not a digit in the string.")
    elif choice == '5':
        # search for '.'
        find = check_period(string)
        if find is True:
            print(find)
            print("There is a period in the string.")
        else:
            print(find)
            print("There is not a period in the string.")
    elif choice == '6':
        # search for 2 consecutive vowels
        find = check_consec_vowel(string)
        if find is True:
            print(find)
            print("There are 2 consecutive vowels in the string.")
        else:
            print(find)
            print("There are not 2 consecutive vowels in the string.")
    elif choice == '7':
        # search for whitespace
        find = check_space(string)
        if find is True:
            print(find)
            print("There is white space in the string.")
        else:
            print(find)
            print("There is not white space in the string.")
    elif choice == '8':
        # search for three repeating letters
        find = check_triple(string)
        if find is True:
            print(find)
            print("There is 3 repeating letters in the string.")
        else:
            print(find)
            print("There is not 3 repeating letters in the string.")
    elif choice == '9':
        # search for 'Hello'
        find = check_Hello(string)
        if find is True:
            print(find)
            print("'Hello' is in the string.")
        else:
            print(find)
            print("'Hello' is not in the string.")
    elif choice == '10':
        # search for an email address
        find = check_email(string)
        if find is True:
            print(find)
            print("There is a email in the string.")
        else:
            print(find)
            print("There is not a email in the string.")
    else:
        # leave loop
        print("Exiting...")
        finish = True
