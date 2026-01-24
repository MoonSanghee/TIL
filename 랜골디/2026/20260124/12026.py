n = int(input())
blocks = input()
# 주어지는 블록의 수와 블록의 형태를 받아줍니다
li = [-1] * n
li[0] = 0
# 각 블록에 도달한 적이 없다고 표시하고 1번 블록에 도달하는데 0의 비용이 든다고 수정해줍니다
for i in range(n):
    if li[i] != -1:
        # 모든 블록을 순회하며 도달한 적 있는지 확인해줍니다
        for j in range(i + 1, n):
            if (blocks[i] == 'B' and blocks[j] == 'O') or (blocks[i] == 'O' and blocks[j] == 'J') or (blocks[i] == 'J' and blocks[j] == 'B'):
                # 도달한 적 있는 블록이라면 이후 블록에서 점프하여 도달할 수 있는 블록을 찾아줍니다
                if li[j] == -1:
                    li[j] = (j - i) ** 2 + li[i]
                else:
                    li[j] = min(li[j], (j - i) ** 2 + li[i])
                # 도달할 수 있는 블록에 처음 도달하는거라면 걸리는 비용으로 수정하고 아니라면 도달하는 비용을 비교하여 작은값으로 갱신하여줍니다

print(li[-1])
# 링크를 만나는데 필요한 최소 에너지를 출력해줍니다