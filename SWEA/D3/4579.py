T = int(input())

for tc in range(1, T + 1):
    word = input()
    # 주어지는 단어를 받아줍니다
    if word == word[::-1]:
        print(f'#{tc} Exist')
        # 단어가 팰린드롬 인지 확인해줍니다
    else:
        for i in range(len(word) // 2):
            if (word[i] == '*' or word[len(word) - 1 - i] == '*'):
                print(f'#{tc} Exist')
                break
            elif word[i] != word[len(word) - 1 - i]:
                print(f'#{tc} Not exist')
                break
        # 주어진 단어가 팰린드롬이 아니라면 와일드카드를 이용한 팰린드롬이 되는지 확인하여 결과를 출력해줍니다