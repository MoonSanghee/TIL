n, k = map(int, input().split())
# 두 수를 받아줍니다
result = []
# 말할 수를 담을 리스트를 만들어줍니다.
for i in range(1, n + 1):
    if i % 10 == k % 10 or i % 10 == (k * 2) % 10:
        continue
    else:
        result.append(i)
# 말할수인지 확인하고 리스트에 값을 담아줍니다.
print(len(result))
print(*result)
# 주어진 조건에 맞추어 출력해줍니다