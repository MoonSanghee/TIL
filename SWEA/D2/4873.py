T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    word = input()
    result = []
    # 주어지는 단어를 받고 결과를 담을 리스트를 만들어줍니다
    for i in word:
        if result and result[-1] == i:
            result.pop()
        else:
            result.append(i)
        # 주어진 단어를 순회하며 글자를 넣었을때 연속한다면 이전 글자도 빼주고 아니라면 글자를 결과에 담아줍니다
    print(f'#{t + 1} {len(result)}')
    # 결과를 주어진 양식에 맞게 출력해줍니다