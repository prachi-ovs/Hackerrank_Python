rows, columns = map(int, input().split())
for i in range(1, rows, 2):
    print((i*".|.").center(columns, "-"))
print("WELCOME".center(columns, "-"))
for i in range(rows-2, 0, -2):
    print((i*".|.").center(columns, "-"))
