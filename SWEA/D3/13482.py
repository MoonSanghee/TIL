T = int(input())
# 테스트케이스의 개수를 받아줍니다
for tc in range(T):
    n = input()
    big, small = int(n), int(n)
    n = list(n)
    # 주어지는 정수를 받고 최소값과 최대값을 담아줍니다
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if i == 0 and n[j] == '0':
                continue
            n[i], n[j] = n[j], n[i]
            new = int(''.join(n))
            big = max(big, new)
            small = min(small, new)
            n[i], n[j] = n[j], n[i]
    # 각 자리를 순회하며 바꿀수 있을때 최대 혹은 최솟값이 갱신되는지 확인하여줍니다
    print(f'#{tc + 1} {small} {big}')
    # 결과를 주어진 양식에 맞게 출력해줍니다