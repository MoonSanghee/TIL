k = int(input())
a, b, c, d = list(map(int, input().split()))
# 정수 k와 4정수를 받아줍니다.
r1 = a * k + b
r2 = c * k + d
# 주어진 계산식에 대입하여줍니다.
if r1 == r2:
    print("Yes",r1)
else:
    print("No")
    # 연속한지 확인하여 조건에 맞게 출력하여줍니다.