T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n, m = map(int, input().split())
    first = set(input().split())
    second = set(input().split())
    # 주어지는 두 문자열의 개수와 문자열 집합을 셋 형태로 받아줍니다
    print(f'#{t + 1} {len(first&second)}')
    # 두 문자열 집합의 교집합을 확인해 공통 개수를 출력해줍니다