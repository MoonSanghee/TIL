n, m = map(int, input().split())
# 생물의 가짓수와 실험의 수를 받아줍니다.
result = [[0, 0] for _ in range(n)]
# 생물의 특성을 담을 변수를 만들어줍니다.
for _ in range(m):
    a, b, c = input().split()
    if b == 'P':
        if c == '1':
            result[int(a) - 1][0] = 1
        else:
            result[int(a) - 1][0] = 2
    else:
        if c == '1':
            result[int(a) - 1][1] = 1
        else:
            result[int(a) - 1][1] = 2
# 입력받은 생물의 특성을 담아줍니다.
big, small = 0, 0

for p, m in result:
    if p == 1 and m == 2:
        big += 1
        small += 1
    elif p == 2 or m == 1:
        continue
    else:
        big += 1
# 생물의 특성을 확인하여 식물이 될수있는 최대값과 최소값을 확인해줍니다.
print(small, big)
# 식물의 최소수와 최대수를 출력해줍니다.