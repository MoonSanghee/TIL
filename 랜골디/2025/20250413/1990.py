a, b = map(int, input().split())
if a % 2 == 0:
    a += 1
if b > 10000000:
    b = 10000000
# 두 수를 받고 시작 수를 홀수로 맞추고 마지막 수의 범위를 제한해줍니다
for i in range(a, b + 1, 2):
    number = str(i)
    if number != number[::-1]:
        continue
    # 팰린드롬이 성립하는지 확인해줍니다
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(number)
    # 소수가 맞는지 확인하여 맞다면 수를 출력해줍니다

print(-1)
# 확인이 끝났으므로 -1을 출력해줍니다