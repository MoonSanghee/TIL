a, m = map(int, input().split())
result = 1
# 주어지는 두 수를 받고 결과를 담을 변수를 설정해줍니다
while True:
    if a * result % m == 1:
        print(result)
        break
    else:
        result += 1
    # 잉여역수라면 값을 출력하고 아니면 1을 더하는 것을 반복하여줍니다