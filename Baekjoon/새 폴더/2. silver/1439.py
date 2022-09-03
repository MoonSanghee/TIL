import sys
sys.stdin = open('test.txt', 'r')

code = str(input())
if len(set(code)) == 1:
    print(0)
else:
    start = code[0]
    n = 0
    for i in range(len(code) - 1):
        if code[i] != code[i + 1]:
            if code[i] == start:
                n += 1
    print(n)