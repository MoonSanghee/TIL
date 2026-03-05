import sys
input = sys.stdin.readline

T = int(input())
# 테스트 케이스가 몇개인지 받아줍니다
for i in range(T):
    N = int(input())
    # 주어지는 부품의 수를 받아줍니다
    A, B = map(int, input().split())
    for _ in range(N):
        u, v = map(int, input().split())
    # 주어지는 기준과 부품의 정보를 받아줍니다
    print(f'Material Management {i + 1}')
    print('Classification ---- End!')
    # 주어진 양식에 맞춰 결과를 출력해줍니다