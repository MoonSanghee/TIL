numbers = list(map(int, input().split()))
# 주어지는 4개의 수를 받아줍니다.
total = []
# 모든 시계수를 담아둘 리스트를 만들어줍니다.
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                notIn = True
                com = [i, j, k, l]
                # 4자리 수 조합을 만들어줍니다.
                for n in range(4):
                    new = com[n:] + com[:n]
                    if new in total:
                        notIn = False
                if notIn:
                    total.append(com)
                # 나왔던 시계수인지 확인하고 아니라면 total에 넣어줍니다.
coms = []
for i in range(4):
    com = numbers[i:] + numbers[:i]
    if com in total:
        p = total.index(com)
        coms.append(p)
# 주어진 4개의 수로 만들수 있는 시계수가 모두 몇번째에 위치하는지 리스트에 담아줍니다.
print(min(coms) + 1)
# 가장 작은 수의 순서를 확인하고 출력해줍니다.