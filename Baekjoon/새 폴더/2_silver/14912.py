n, d = map(int, input().split())
# 범위와 확인할 수를 받아줍니다.
dictionary = dict()
for i in range(10):
    key = str(i)
    dictionary[key] = 0
# 딕셔너리를 만들어 0부터 9까지의 값을 0으로 설정해줍니다.

for i in range(1, n + 1):
    for j in str(i):
        dictionary[j] += 1
    # 범위안의 수를 순회하며 각 자리 수를 더해줍니다.
print(dictionary[str(d)])
# 수의 빈도를 출력해줍니다.