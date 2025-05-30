rgb = list(map(int, input().split()))
result = 0
# 세 가지 색의 공의 개수를 리스트에 담고 필요한 박스의 수를 담을 설정해줍니다
for i in range(3):
    result += rgb[i] // 3
    rgb[i] %= 3
# 같은 색을 3개씩 같은 상자에 넣어주고 남은 공의 개수로 값을 수정해줍니다
zero = 0
while True:
    if sum(rgb) == 0:
        break
    # 남는 공이 없을때까지 진행합니다
    result += 1
    # 남는 공이 있다면 상자를 1개 더 써줍니다
    for i in range(3):
        if rgb[i] == 0:
            zero += 1
    # 공이 없는 색이 몇개인지 확인해줍니다
    if zero == 2:
        for i in range(3):
            rgb[i] = 0
    # 2가지 색의 공이 없다면 모두 한 상자에 담을수 있으므로 모든 공을 0으로 수정해줍니다
    else:
        for i in range(3):
            if rgb[i]:
                rgb[i] -= 1
    # 아니면 남은 공을 색깔별로 1개씩 같이 담아줍니다

print(result)
# 필요한 상자의 수를 출력해줍니다