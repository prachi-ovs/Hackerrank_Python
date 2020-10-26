# Without space padding
def print_formatted(n):
    allForms = []
    allDigits = []
    for i in range(1, n+1):
        allFormats = ' '.join(map(str, [i, oct(i)[2:], hex(i)[2:], bin(i)[2:]]))
        allDigits.append(allFormats)
    print('\n'.join(allDigits))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)