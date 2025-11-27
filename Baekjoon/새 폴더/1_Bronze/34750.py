n = int(input())
# 받은 용돈의 액수를 받아줍니다
if n >= 1000000:
    print(int(n * 0.2), int(n * 0.8))
elif n >= 500000:
    print(int(n * 0.15), int(n * 0.85))
elif n >= 100000:
    print(int(n * 0.1), int(n * 0.9))
else:
    print(int(n * 0.05), int(n * 0.95))
# 주어진 범위에따라 부모님께 드리는 금액과 남은 금액을 출력해줍니다