def swap_case(s):
    newstring =''
    for a in s:
# Checking for lowercase letter and converting to uppercase.
        if (a.isupper()) == True:
            newstring+=(a.lower())
# Checking for uppercase letter and converting to lowercase.
        elif (a.islower()) == True:
            newstring+=(a.upper())
# Checking for whitespace letter and adding it to the new string
        elif (a.isspace()) == True:
            newstring+= a
# Checking for numeric and adding it to the new string
        elif (a.isnumeric()) == True:
            newstring+= a
# Checking for non alphanumeric characters and adding it to the new string
        elif (a.isalnum()) == False:
            newstring+= a


    return newstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)