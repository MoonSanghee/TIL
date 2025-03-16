n = int(input())
buildings = [0]
result = 0
# 빌딩의 높이를 담을 리스트와 개수를 담을 변수를 설정해줍니다
for _ in range(n):
    x, y = map(int, input().split())
    if y > buildings[-1]:
        buildings.append(y)
        # 빌딩의 마지막 높이보다 큰 건물이 보인다면 리스트에 추가해줍니다
    elif y == buildings[-1]:
        continue
    else:
        while buildings[-1] > y:
            result += 1
            buildings.pop()
        if buildings[-1] != y:
            buildings.append(y)
        # 빌딩의 마지막 높이보다 보이는 빌딩이 낮다면 높은 빌딩들을 모두 빼고 마지막 빌딩의 높이가 다른 경우 
        # 빌딩이 하나 더 추가되므로 리스트에 건물의 높이를 넣어줍니다
for i in range(len(buildings) - 1):
    if buildings[i] != buildings[i + 1]:
        result += 1
# 리스트에서 아직 남은 빌딩을 확인하여 빌딩의 개수를 더해줍니다
print(result)
# 결과를 출력해줍니다