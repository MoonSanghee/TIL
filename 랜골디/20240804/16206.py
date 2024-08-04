n, m = map(int, input().split())
cakes = list(map(int,input().split()))
cakes.sort()
# 케이크의 개수와 자를 횟수를 받고 케이크를 오름차순으로 정렬해줍니다.
result = 0
# 총 먹을수있는 케이크의 개수를 담을 변수를 설정해줍니다.
for i in range(n):
    if cakes[i] % 10 == 0:
        # 케이크가 10의 배수라면 
        cut = (cakes[i] // 10) - 1
        if cakes[i] == 10:
            result += 1
            cakes[i] -= 10
        elif cut <= m:
            m -= cut
            result += cut + 1
            cakes[i] = 0
        else:
            result += m
            cakes[i] -= m * 10
            m = 0
        # 자를수 있는 횟수와 비교하여 만들어진 먹을수있는 개수값을 갱신해줍니다.

if m > 0:
    for i in cakes:
        if m == 0:
            break
        elif i < m * 10:
            m -= i // 10
            result += i // 10
            i = 0
        else:
            result += m
            m = 0
# 자를수있는 횟수가 남았다면 크기가 10 이상의 케이크들을 자르며 먹을수 있는 횟수를 더해줍니다.

print(result)
# 결과를 출력해줍니다.