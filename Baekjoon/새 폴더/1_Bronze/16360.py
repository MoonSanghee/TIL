d = {
    'a' : 'as',
    'i' : 'ios',
    'y' : 'ios',
    'l' : 'les',
    'n' : 'anes',
    'o' : 'os',
    'r' : 'res',
    't' : 'tas',
    'u' : 'us',
    'v' : 'ves',
    'w' : 'was',
}

n = int(input())
# 단어의 개수를 받아줍니다
for _ in range(n):
    word = input()
    # 단어를 받아줍니다
    if word[len(word) - 2:] == 'ne':
        result = word[:-2] + 'anes'
    elif word[len(word) - 1] in d:
        result = word[:-1] + d[word[-1]]
    else:
        result = word + 'us'
    # 끝 문자를 확인하여 주어진 양식대로 수정하여줍니다
    print(result)
    # 결과를 출력해줍니다