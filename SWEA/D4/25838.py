T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n = int(input())
    word = input()
    # 주어지는 단어의 길이와 단어를 받아줍니다
    result = []
    # 남은 단어를 담아둘 변수를 설정해줍니다
    for i in word:
        result.append(i)
        if len(result) > 2 and result[-3:] == ['f', 'o', 'x']:
            result.pop()
            result.pop()
            result.pop()
    # 리스트에 담긴 마지막 세 글자가 fox이라면 세개의 글자를 빼줍니다
    print(len(result))
    # 남은 단어의 길이를 출력해줍니다