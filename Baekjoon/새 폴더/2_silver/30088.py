t = int(input())
# 조의 개수를 받아줍니다.
groups = []
for _ in range(t):
    numbers = list(map(int, input().split()))
    groups.append(sum(numbers[1:]))
# 각 조별로 상담을 받는데 필요한 시간을 리스트에 담아줍니다.
groups.sort(reverse=True)
# 시간이 걸리는것을 내림차순으로 정렬해줍니다.
result = 0
for i in range(len(groups)):
    result += (i + 1) * groups[i]
print(result)
# 최소값을 출력해줍니다.