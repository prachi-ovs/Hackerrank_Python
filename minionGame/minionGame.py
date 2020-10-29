def minion_game(string):
    vowels = ['A','E','I','O','U']
    subStrings = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
    kevinsWords = [i for i in subStrings if i[0] in vowels]
    stuartsWords = [i for i in subStrings if i[0] not in vowels]
    if len(kevinsWords) > len(stuartsWords):
        print("Kevin", len(kevinsWords))
    elif len(stuartsWords) > len(kevinsWords):
        print("Stuart", len(stuartsWords))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)