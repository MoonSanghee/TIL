n = int(input())
total = 0
towns = []
for _ in range(n):
    position, people = map(int, input().split())
    towns.append((position, people))
    total += people
towns.sort(key=lambda x : x[0])
# 마을의 수를 받고 마을의 위치와 사람의 수를 받아 마을 정보 리스트에 담고 전체 주민의 합을 구해줍니다
# 마을을 거리순으로 정렬해줍니다
count = 0
for position, people in towns:
    count += people
    if count >= total / 2:
        print(position)
        break
    # 마을을 차례대로 순회하며 누적되는 마을사람의 수가 과반이 넘는 순간을 찾아 출력해줍니다