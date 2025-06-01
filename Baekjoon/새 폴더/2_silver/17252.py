n = int(input())
# 주어지는 수를 받아줍니다
if n == 0:
    print("NO")
    # n이 0이라면 3의 0승보다 작으므로 3의 거듭제곱의 합으로 나타낼 수가 없습니다
else:
    while True:
        if n % 3 == 2:
            print("NO")
            break
        elif n == 0:
            print("YES")
            break
        n //= 3
    # 3으로 나누었을때 나머지가 2인 경우가 존재한다면 3의 거듭제곱으로만 나타낼 수 없고 아니면 3의 거듭제곱으로 나타낼 수 있습니다