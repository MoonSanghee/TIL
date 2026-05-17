TC = int(input())
# 테스트 케이스가 몇개인지 받아줍니다
for t in range(TC):
    word = input()
    # 주어지는 단어를 받아줍니다
    result = 1
    # 결과를 담을 변수를 설정해줍니다
    for i in range(len(word)):
        for j in range(i + result, len(word) + 1):
            made = word[i:j]
            if made == made[::-1]:
                result = len(made)
    # 단어를 순회하며 가장 긴 팰린드롬 영역을 찾아줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 방식에 맞춰 출력해줍니다