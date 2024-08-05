w, p = map(int, input().split())
n = list(map(int, input().split()))
# 전체 폭과 파티션의 개수 파티션의 위치를 받아줍니다.
rooms = [n[0]]
for i in range(p - 1):
    rooms.append(n[i + 1] - n[i])
rooms.append(w - n[-1])
# 연속한 파티션을 설치하였을때 생기는 공간의 크기를 받아줍니다.
result = rooms

for i in  range(p + 2):
    for j in range(i + 2, p + 2):
        result.append(sum(rooms[i:j]))
# 임의의 두 파티션을 설치하였을때 생기는 공간의 크기를 담아줍니다.

print(*sorted(list(set(result))))
# 중복된 값을 제거한후 정렬한 값을 출력해줍니다.