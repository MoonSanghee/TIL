a, b = map(int, input().split())
# 두 수를 받아줍니다.
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print(i, a // i, b // i)
    # 1부터 작은 수까지 확인하며 두수의 공약수가 나오면 요청받은 형식에 맞추어 출력해줍니다.