n = int(input())
# 테스트 케이스의 수를 받아줍니다.
for _ in range(n):
    word = input()
    if len(word) % 2 == 1:
        word *= 2
    # 게임을 할 단어를 받아줍니다. 단어의 길이가 홀수이면 2번 왕복해야 패턴이 나오므로 단어를 2로 곱해줍니다.
    hwan = ''
    wook = ''
    for i in range(len(word)):
        if i % 2 == 0:
            hwan += word[i]
        else:
            wook += word[i]
    # 두 사람이 외칠 문자를 받아줍니다.
    print(hwan)
    print(wook)
    # 두 사람이 외칠 패턴을 차례대로 출력해줍니다.