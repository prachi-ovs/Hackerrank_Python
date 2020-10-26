# Complete the solve function below.
def solve(name):
    l = name.split(' ')
    newName = ' '.join((word.capitalize() for word in l))
    return newName


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

