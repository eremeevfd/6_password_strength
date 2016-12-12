import re
import os


def password_in_blacklist(password):
    password_blacklist = []
    if os.path.exists("62kcmnpass.txt"):
        with open("62kcmnpass.txt") as opened:
            for line in opened:
                password_blacklist.append(line.strip())
    return password in password_blacklist


def check_password_length_return_score(password):
    if len(password) >= 13:
        return 2
    elif len(password) >= 8:
        return 1
    else:
        return 0


def count_password_digits(password):
    digits_list = re.findall(r'\d', password)
    return digits_list


def check_password_for_lowercase_return_score(password):
    return re.search(r'[a-z]', password) is not None


def count_password_uppercase(password):
    uppercase_list = re.findall(r'[A-Z]', password)
    return uppercase_list


def count_password_symbols(password):
    symbols_list = re.findall(r'[_\W]', password)
    return symbols_list

def check_password_for_some_criteria(criteria):
    if len(criteria) > 1:
        return 2
    elif len(criteria) == 1:
        return 1
    else:
        return 0

def get_password_strength(password):
    password_score = 1
    if password_in_blacklist(password):
        return password_score
    else:
        return (password_score
                + check_password_length_return_score(password)
                + check_password_for_some_criteria(count_password_digits(password))
                + check_password_for_lowercase_return_score(password)
                + check_password_for_some_criteria(count_password_uppercase(password))
                + check_password_for_some_criteria(count_password_symbols(password))
                )


if __name__ == '__main__':
    print("Your password strength score is: " + str(get_password_strength(input("Enter your password: "))))
