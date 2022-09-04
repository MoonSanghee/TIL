test = int(input())
for t in range(1, test + 1):
    word = input()
    hyphen = [0]*(len(word) + 1)
    n = int(input())
    pos = list(map(int, input().split()))
    for i in pos:
        hyphen[i] += 1
    word = ' ' + word
    result = ''
    for i in range(len(word)):
        result += word[i] + hyphen[i]*'-'
    result = result.replace(' ', '')
    print(f'#{t} {result}')