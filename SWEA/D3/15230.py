T = int(input())
base = 'abcdefghijklmnopqrstuvwxyz'
# 주어지는 테스트케이스의 수와 알파벳 순서를 받아줍니다
for t in range(T):
    word = input()
    result = 0
    # 주어지는 단어를 받고 맞게적힌 알파벳의 숫자를 담을 변수를 설정해줍니다
    for i in range(len(word)):
        if base[i] == word[i]:
            result += 1
        else:
            break
    # 맞게 적힌 알파벳을 확인해줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다