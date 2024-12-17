n = int(input())
# 주어지는 냉장고의 용량을 받아줍니다
result = 1e9
# 최대 겉넓이를 설정해줍니다
divisor = []
for i in range(1, n + 1):
    if n % i == 0:
        divisor.append(i)
# 주어진 냉장고 용량의 약수를 구해줍니다
for i in divisor:
    for j in divisor:
        for k in divisor:
            if i * j * k == n:
                if result > i * j + j * k + k * i:
                    result = i * j + j * k + k * i
                    answer = [i, j, k]
# 임의의 약수 3개의 곱이 용량이 된다면 겉넓이가 더 작아지는지 확인하고 값을 갱신해줍니다
print(*answer)
# 결과를 출력해줍니다