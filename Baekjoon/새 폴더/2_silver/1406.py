import sys

word = list(sys.stdin.readline().strip())
back = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == 'P':
        word.append(command[1])
    elif command[0] == 'L':
        if word:
            back.append(word.pop())
    elif command[0] == 'D':
        if back:
            word.append(back.pop())
    else:
        if word:
            word.pop()
word += back[::-1]
print(''.join(word))