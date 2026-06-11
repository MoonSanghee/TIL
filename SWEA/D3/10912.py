T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    word = list(input())
    word.sort(reverse=True)
    # 주어지는 단어를 리스트형태로 받아 내림차순으로 정렬해줍니다
    check = []
    while word:
        x = word.pop()
        if check != [] and check[-1] == x:
            check.pop()
        else:
            check.append(x)
    # 짝을 이루지 못하는 문자들을 찾아줍니다
    result = ''.join(check)
    if result == '':
        result = 'Good'
    # 모두 짝을 맞춘다면 주어진 값으로 바꾸어줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다