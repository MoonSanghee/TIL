T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    word1 = input()
    word2 = input()
    # 두 단어를 받아줍니다
    if word1 in word2:
        print(f'#{t + 1} 1')
    else:
        print(f'#{t + 1} 0')
    # 2번째로 주어진 단어 안에 첫 번째 단어가 존재하는지 확인하여 결과를 출력해줍니다