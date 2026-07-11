T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    word = input()
    # 주어지는 단어를 받아줍니다
    if word == word[::-1]:
        print(f'#{t + 1} 1')
    else:
        print(f'#{t + 1} 0')
    # 단어가 회문인지 확인하여 결과를 주어진 양식에 맞춰 출력해줍니다