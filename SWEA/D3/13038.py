T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    n = int(input())
    schedule = list(map(int, input().split()))
    minimum = 10e9
    # 들으려는 수업일수와 수업 일정을 받고 결과를 담을 변수를 설정해줍니다
    for i in range(7):
        now = i
        remain = n
        passed = 0
        while remain:
            if schedule[now] == 1:
                remain -= 1
            passed += 1
            now = (now + 1) % 7
        minimum = min(minimum, passed)
        # 각 요일에서 시작하여 원하는 수업일수를 모두 듣는데 걸리는 최소일수를 확인해줍니다
    
    print(f'#{t + 1} {minimum}')
    # 결과를 주어진 양식에 맞게 출력해줍니다