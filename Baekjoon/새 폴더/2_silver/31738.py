n, m = map(int, input().split())
result = 1
# n과 m을 받아줍니다.
# 나머지를 1로 설정해줍니다.
if n >= m:
    result = 0
    # n이 m 이상이라면 n!은 m을 포함하므로 나머지를 0으로 갱신해줍니다.
else:
    while n:
        result *= n
        result %= m
        if result == 0:
            break
        n -= 1
        # n부터 1씩 줄여가며 수를 곱하고 m을 나누는것을 n이 1일때까지 반복해줍니다.
        # 나머지가 0이되면 어떤수를 더 곱해도 나머지가 0일것이므로 계산을 멈춥니다.

print(result)
# 나머지를 출력해줍니다.