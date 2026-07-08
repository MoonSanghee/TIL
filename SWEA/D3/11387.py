T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    D, L, N = map(int, input().split())
    result = 0
    cnt = 0
    # 주어지는 변수들을 받고 공격 횟수와 결과를 담을 변수를 설정해줍니다
    while cnt < N:
        damage = D * (1 + cnt * (L / 100))
        result += damage
        cnt += 1
	# 공격 횟수에 따라 데미지를 계산해줍니다
    result = int(result)
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다