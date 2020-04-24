# Elizabeth Fuller
# 4/23/20
# RegEx

import re

def check_q(string):
    x = re.search('q', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_the(string):
    x = re.search('the', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_ast(string):
    x = re.search('\*', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_digit(string):
    x = re.search('\d', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_period(string):
    x = re.search('\.', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_consec_vowel(string):
    x = re.search('q', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_space(string):
    x = re.search('q', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_triple(string):
    x = re.search('q', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_Hello(string):
    x = re.search('Hello', string)
    if (x):
        found = True
    else:
        found = False
    return found


def check_email(string):
    x = re.search('q', string)
    if (x):
        found = True
    else:
        found = False
    return found


print("Enter string here:")
string = input("> ")

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
    Check for triple letters [8]
    Check for 'Hello' [9]
    Check for email [10]
    Exit [11]""")

    choice = int(input("> "))
    if choice == 1:
        find = check_q(string)
        if find is True:
            print(find)
            print("There is a 'q' in the string.")
        else:
            print(find)
            print("there is not a 'q' in the string.")
    elif choice == 2:
        find = check_the(string)
        if find is True:
            print(find)
            print("There is a 'the' in the string.")
        else:
            print(find)
            print("there is not a 'the' in the string.")
    elif choice == 3:
        check_ast(string)
    elif choice == 4:
        check_digit(string)
    elif choice == 5:
        check_period(string)
    elif choice == 6:
        check_consec_vowel(string)
    elif choice == 7:
        check_space(string)
    elif choice == 8:
        check_triple(string)
    elif choice == 9:
        check_Hello(string)
    elif choice == 10:
        check_email(string)
    elif choice == 11:
        finish = True
