n, m = map(int, input().split())
# 심사위원의 수와 문제의 개수를 받아줍니다
result = 0
# 출제될 문제의 수를 담을 변수를 설정해줍니다
for _ in range(n):
    cnt = 0
    for i in input():
        if i == 'O':
            cnt += 1
    if cnt > m // 2:
        result += 1
    # 주어지는 문제를 순회하며 채점 결과를 확인해 출제될 수 있는지 확인해줍니다
print(result)
# 결과를 출력해줍니다