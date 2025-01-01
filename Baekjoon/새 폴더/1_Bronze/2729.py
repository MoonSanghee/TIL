n = int(input())
# 주어지는 수가 몇 쌍인지 받아줍니다
for _ in range(n):
    a, b = input().split()
    a = int(a, 2)
    b = int(b, 2)
    # 두 이진수를 10진수로 변환해줍니다
    result = bin(a + b)[2:]
    print(result)
    # 주어진 두 수의 합을 2진수로 전환해 출력해줍니다