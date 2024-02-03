from math import gcd

n = int(input())
circles = list(map(int, input().split()))
# 원의 수와 원을 받아줍니다.
for i in range(1, n):
    num = gcd(circles[0], circles[i])
    # 두번째 원부터 첫 번째 원과 의 최대공약수를 구해줍니다.
    print(f'{circles[0] // num}/{circles[i] // num}')
    # 첫 바퀴가 돌 때 다음 바퀴가 얼마나 도는지 제시된 형태로 출력해줍니다.