def count_substring(s, ss):
    counts =0
    stringList = list(s)
    substringList = list(ss)
    stringLength, substringLength = len(stringList), len(substringList)
    for i in range(stringLength):
        if stringList[i:i+len(substringList)] == substringList:
            counts += 1
    return counts


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)

