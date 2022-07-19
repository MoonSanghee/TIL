a = input()
b = list(a)
for i in b:
    if ord(i) in range(97, 123):
        i = ord(i) - 96
        print(i, end = ' ')
    elif ord(i) in range(65, 91):
        i = ord(i) - 64
        print(i, end = ' ')
