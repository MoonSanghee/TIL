m, n, l = map(int, input().split())
# 세 정수를 받아줍니다.
p = list(map(int, input().split()))
p.sort()
animals = [list(map(int, input().split())) for _ in range(n)]
result = 0
# 사대의 위치를 받아 오름차순으로 정렬해줍고 동물들의 위치를 받아줍니다.
for x, y in animals:
    limit = l - y
    s = 0
    e = m - 1
    # 동물과의 x 거리를 구하고 처음과 끝 인덱스값을 구해줍니다.
    while s <= e:
        mid = (s + e) // 2
        if p[mid] < x - limit:
            s = mid + 1
        elif p[mid] > x + limit:
            e = mid - 1
        else:
            result += 1
            break
        # 이분탐색을 통해서 동물이 사거리안에 존재하는 사대가 있는지 확인하고 있다면 result에 1을 추가해줍니다.

print(result)
# result에 담긴 맞출수있는 동물의 수를 출력해줍니다.