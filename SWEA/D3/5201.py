T = int(input())
# 테스트 케이스의 수를 받아줍니다
for t in range(T):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    # 주어지는 변수들을 받아줍니다
    wi.sort(reverse=True)
    ti.sort(reverse=True)
    # 두 리스트를 내림차순으로 정렬해줍니다
    result = 0
    j = 0
    # 결과를 담을 변수와 확인할 컨테이너의 차례를 담을 변수를 설정해줍니다
    for i in range(N):
        if wi[i] <= ti[j]:
            result += wi[i]
            j += 1
            if j == M:
                break
    # 화물을 실을 수 있는지 확인해줍니다
    print(f'#{t + 1} {result}')
    # 결과를 출력해줍니다