n = int(input())
cnt = list(map(int, input().split()))
# 치킨을 몇마리 시키는지와 각 치킨을 선호하는 사람의 수를 받아줍니다
result = 0
# 결과를 담을 변수를 설정해줍니다
for i in cnt:
    result += min(i, n)
# 선호하는 치킨을 먹을수 있는 사람의 수를 더해줍니다
print(result)
# 결과를 출력해줍니다