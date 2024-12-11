k1, o1, k2, o2, k3 = input().split()
k1, k2, k3 = int(k1), int(k2), int(k3)
# 주어지는 기호와 정수들을 받아줍니다
def cal(x, y, o):
    if o == '+':
        n = x + y
    elif o == '-':
        n = x - y
    elif o == '*':
        n = x * y
    else:
        n = abs(x) // abs(y)
        if x * y < 0:
            n *= -1
    return n
# 기호에 따라 진행할 계산을 실행하고 결과값을 리턴해줍니다

result1 = cal(cal(k1, k2, o1), k3, o2)
result2 = cal(k1, cal(k2, k3, o2), o1)
# 두 순서의 계산을 실행해줍니다
print(min(result1, result2))
print(max(result1, result2))
# 작은수와 큰 수 순으로 출력해줍니다