# Elizabeth Fuller
# 4/23/20
# RegEx


def check_q(string):
    return


def check_the(string):
    return


def check_ast(string):
    return


def check_digit(string):
    return


def check_period(string):
    return


def check_consec_vowel(string):
    return


def check_space(string):
    return


def check_triple(string):
    return


def check_Hello(string):
    return


def check_email(string):
    return


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
        check_q(string)
    elif choice == 2:
        check_the(string)
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
