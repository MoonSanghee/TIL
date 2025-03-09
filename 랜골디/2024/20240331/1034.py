n, m = map(int, input().split())
lamps = [input() for _ in range(n)]
k = int(input())
# 주어지는 탁자의 크기와 램프가 켜져있는 상태를 받고 버튼을 몇 번 누를것인지 받아줍니다
result = 0
# 가장 많이 켜지는 경우를 담을 변수를 설정해줍니다.
for i in range(n):
    zero = 0
    for j in range(m):
        if lamps[i][j] == '0':
            zero += 1
    # 각 행에서 0의 개수를 확인해줍니다.
    if (zero % 2) == (k % 2) and k >= zero:
        cnt = 0
        for j in range(n):
            if lamps[i] == lamps[j]:
                cnt += 1
        result = max(result, cnt)
    # 각 행에 대하여 원하는 횟수로 불을 킬 수 있는지 확인하고 불을 킬 수 있다면
    # 같은 방식으로 몇개의 불을 킬수 있는지 확인하여 최대값과 비교하여줍니다.
print(result)
# 가장 많은 불이 켜진 수를 출력해줍니다.