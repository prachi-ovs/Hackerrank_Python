def swap_case(s):
    newstring = ''
    for a in s:
        # Checking for lowercase letter and converting to uppercase.
        if a.isupper():
            newstring += (a.lower())
        # Checking for uppercase letter and converting to lowercase.
        elif a.islower():
            newstring += (a.upper())
        # Checking for whitespace, numeric or non alphanumeric letter and adding it to the new string
        elif a.isspace() or a.isnumeric() or not (a.isalnum()):
            newstring += a

    return newstring


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
