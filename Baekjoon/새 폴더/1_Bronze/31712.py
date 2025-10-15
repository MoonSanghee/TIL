c = []
d = []

for i in range(3):
    a, b = map(int, input().split())
    c.append(a)
    d.append(b)
# 스킬의 사용 주기와 데미지를 리스트에 담아줍니다
energy = int(input())
result = 0
energy -= sum(d)
# 핑크빈의 체력을 받아 0초에 모든 스킬 데미지를 적용해줍니다
while True:
    if energy <= 0:
        print(result)
        break
    # 에너지가 모두 달았다면 시간을 출력하고 반복을 멈추어줍니다
    result += 1
    for i in range(3):
        if result % c[i] == 0:
            energy -= d[i]
    # 반복이 진행되었다면 시간을 1초 지나고 사용 가능한 스킬을 사용한 결과를 적용해줍니다