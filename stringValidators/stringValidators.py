def string_validator(s):
    flag_alnum = 0
    flag_alpha = 0
    flag_num = 0
    flag_lower = 0
    flag_upper = 0
    for i in s:
        flag_alnum = 1 if i.isalnum() else 0
        flag_alpha = 1 if i.isalpha() else 0
        flag_num = 1 if i.isdigit() else 0
        flag_lower = 1 if i.islower() else 0
        flag_upper = 1 if i.isupper() else 0

    print("True" if flag_alnum == 1 else "False")
    print("True" if flag_alpha == 1 else "False")
    print("True" if flag_num == 1 else "False")
    print("True" if flag_lower == 1 else "False")
    print("True" if flag_upper == 1 else "False")


if __name__ == '__main__':
    string = input()
    string_validator(string)
