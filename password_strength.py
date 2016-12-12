import re
import os


def password_in_blacklist(password):
    password_blacklist = []
    if os.path.exists("62kcmnpass.txt"):
        with open("62kcmnpass.txt") as opened:
            for line in opened:
                password_blacklist.append(line.strip())
    return password in password_blacklist


def password_length_score(password):
    if len(password) >= 13:
        return 2
    elif len(password) >= 8:
        return 1
    else:
        return 0


def password_with_digits_score(password):
    digits_list = re.findall(r'\d', password)
    if len(digits_list) > 1:
        return 2
    elif len(digits_list) == 1:
        return 1
    else:
        return 0


def password_with_lowercase_score(password):
    return re.search(r'[a-z]', password) is not None


def password_with_some_uppercases_score(password):
    uppercase_list = re.findall(r'[A-Z]', password)
    if len(uppercase_list) > 1:
        return 2
    elif len(uppercase_list) == 1:
        return 1
    else:
        return 0


def password_with_some_symbols_score(password):
    symbols_list = re.findall(r'[_\W]', password)
    if len(symbols_list) > 1:
        return 2
    elif len(symbols_list) == 1:
        return 1
    else:
        return 0


def get_password_strength(password):
    password_score = 1
    if password_in_blacklist(password):
        return password_score
    else:
        return (password_score
                + password_length_score(password)
                + password_with_digits_score(password)
                + password_with_lowercase_score(password)
                + password_with_some_uppercases_score(password)
                + password_with_some_symbols_score(password)
                )


if __name__ == '__main__':
    print("Your password strength score is: " + str(get_password_strength(input("Enter your password: "))))
