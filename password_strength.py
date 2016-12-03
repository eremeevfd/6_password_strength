import re


def password_in_blacklist(password):
    password_blacklist = ('Password1', 'Welcome1', 'P@ssword', 'Summer1!', 'password', 'Fa$hion1', 'Hello123',
                          'Welcome123', '123456q@', 'P@ssword1', '123456', '123456a', '123456abc', 'qwerty',
                          'qwerty123', 'qwerty123456')
    return password in password_blacklist


def password_check_length(password):
    if len(password) >= 13:
        return 2
    elif len(password) >= 8:
        return 1
    else:
        return 0


def password_with_digits(password):
    digits_list = re.findall(r'\d', password)
    if len(digits_list) > 1:
        return 2
    elif len(digits_list) == 1:
        return 1
    else:
        return 0


def password_with_lowercase(password):
    return re.search(r'[a-z]', password) is not None


def password_with_some_uppercases(password):
    uppercase_list = re.findall(r'[A-Z]', password)
    if len(uppercase_list) > 1:
        return 2
    elif len(uppercase_list) == 1:
        return 1
    else:
        return 0


def password_with_some_symbols(password):
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
                + password_check_length(password)
                + password_with_digits(password)
                + password_with_lowercase(password)
                + password_with_some_uppercases(password)
                + password_with_some_symbols(password)
                )


if __name__ == '__main__':
    print("Your password strength score is: " + str(get_password_strength(input("Enter your password: "))))
