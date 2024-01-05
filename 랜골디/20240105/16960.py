n, m = map(int, input().split())
switchs = dict()
lamps = [0] * m
# 램프와 스위치의 개수를 받고 스위치 정보를 담을 딕셔너리와 램프를 작동하게하는 스위치의 개수를 확인할 리스트를 만들어줍니다.

for i in range(n):
    switch = list(map(int, input().split()))[1:]
    for j in switch:
        lamps[j - 1] += 1
    switchs[i] = switch
# 스위치로 작동할 수 있는 램프를 표시해주고 스위치 정보를 담아줍니다.

for i in range(n):
    isPossible = True
    for j in switchs[i]:
        if lamps[j - 1] == 1:
            isPossible = False
            break
    if isPossible:
        print(1)
        break
else:
    print(0)
# 스위치를 순회하며 각 스위치가 없어도 모든 램프가 불이 들어오는지 확인하고 없어도 되는 버튼이 존재한다면 1 없다면 0을 출력해줍니다.