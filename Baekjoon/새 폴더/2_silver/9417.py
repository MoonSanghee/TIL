from math import gcd

t = int(input())
# 입력되는 케이스의 수를 받아줍니다.
for _ in range(t):
    numbers = list(map(int, input().split()))
    result = 1
    # 주어지는 수열을 받고 최대 공약수를 담을 변수를 정해줍니다.
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num = gcd(numbers[i], numbers[j])
            result = max(num, result)
    # 두 수를 순회하며 최대 공약수를 확인하여 값을 갱신해줍니다.
    print(result)
    # 결과를 출력해줍니다.