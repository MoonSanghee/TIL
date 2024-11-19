n = int(input())
numbers = list(map(int, input().split()))
# 수의 개수와 주어지는 수를 받아줍니다
for i in numbers:
    result = 0
    for j in range(1, i):
        if i % j == 0:
            result += j
    # 진약수를 찾아 더해줍니다
    if result < i:
        print("Deficient")
    elif result == i:
        print("Perfect")
    else:
        print("Abundant")
    # 진약수와 주어진 수를 비교하여 결과를 출력해줍니다