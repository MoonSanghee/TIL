m, n = map(int, input().split())
space = []
# 주어지는 우주들의 정보를 받아줍니다
for _ in range(m):
    arr = list(map(int, input().split()))
    check = sorted(arr)
    idx = [check.index(i) for i in arr]
    space.append(idx)
    # 행성의 크기를 오름차순으로 정렬하여 행성의 번호로 수정한 리스트를 모아줍니다

result = 0

for i in range(m):
    for j in range(1 + i, m):
        if space[i] == space[j]:
            result += 1
# 두 우주를 비교하여 배치 형태가 동일한 쌍이 얼마나 있는지 확인해줍니다
print(result)
# 결과를 출력해줍니다