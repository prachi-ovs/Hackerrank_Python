def wrap(s, width):
    wordSlice = []
    while s:
        wordSlice.append(s[0:width])
        s = s[width:]
    return '\n'.join(wordSlice)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)