T = int(input())
d = {
    'b' : 'd',
    'd' : 'b',
    'q' : 'p',
    'p' : 'q',
}
# 테스트 케이스의 수를 받고 뒤집는 문자쌍을 딕셔너리에 담아줍니다
for t in range(T):
    word = input()[::-1]
    result = ''
    # 주어지는 단어를 받아 거꾸로 뒤집어주고 결과를 담을 변수를 설정해줍니다
    for i in word:
        result += d[i]
    # 뒤집은 단어를 순회하며 딕셔너리의 밸류값으로 결과에 담아줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 형식에 맞춰 출력해줍니다