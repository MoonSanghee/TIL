T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    n = int(input())
    word = input()
    # 단어의 길이와 단어를 받아줍니다
    if n % 2:
        print(f'#{t + 1} No')
        # 단어의 길이가 홀수라면 단어를 두 번 반복해 만들수 없습니다
    else:
        if word[:n // 2] == word[n // 2:]:
            print(f'#{t + 1} Yes')
        else:
            print(f'#{t + 1} No')
        # 짝수라면 두 번 반복되는지 확인하여 결과를 주어진 양식에 맞게 출력해줍니다