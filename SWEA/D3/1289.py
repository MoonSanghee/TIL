import sys
sys.stdin = open('1289_input.txt', 'r')

test_case = int(input())
for test in range(1, test_case + 1):
    word = input()
    cnt = 0
    if word[0] == '1':
        cnt += 1
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            cnt += 1
    print(f'#{test} {cnt}')