n = int(input())
# 계산이 얼마나 주어지는지 받아줍니다
for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)
    # 두 정수를 받아 합을 출력해줍니다