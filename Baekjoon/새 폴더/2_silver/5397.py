t = int(input())
for tc in range(t):
    command = input()
    cursor = 0
    word = []
    for i in command:
        if i =='<':
            if cursor > 0:
                cursor -= 1
        elif i == '>':
            if cursor < len(word):
                cursor += 1
        elif i == '-':
            if cursor != 0:
                word.pop(cursor - 1)
                cursor -= 1
        else:
            word.insert(cursor, i)
            cursor += 1
    print(''.join(word))