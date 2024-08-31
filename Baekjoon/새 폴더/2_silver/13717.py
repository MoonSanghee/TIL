n = int(input())
# 가지고있는 포켓몬이 몇종인지 받아줍니다.
cnt = 0
highest = 0
# 전체 진화시킨수를 담을 변수와 가장 많이 진화한 수를 담을 변수를 만들어줍니다.
for _ in range(n):
    name = input()
    k, m = map(int, input().split())
    # 포켓몬의 정보를 받아줍니다.
    evolution = 0
    while k <= m:
        m -= k
        m += 2
        evolution += 1
    cnt += evolution
    # 진화시킬수있는지 확인하여 진화시키는 횟수는 구하고 cnt에 더해줍니다.
    if evolution > highest:
        highest = evolution
        most = name
    # 가장 많이 진화시킨수가 변화한다면 이름을 갱신해줍니다

print(cnt)
print(most)
# 요구받은 출력을 실행해줍니다.