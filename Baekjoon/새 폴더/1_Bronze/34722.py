n = int(input())
result = 0
# 확인할 사람의 수를 받고 출제자격이 있는 사람의 수를 담을 변수를 설정해줍니다
for _ in range(n):
    s, c, a, r = map(int, input().split())
    if s >= 1000 or c >= 1600 or a >= 1500 or (r != -1 and r <= 30):
        result += 1
    # 주어진 조건을 비교하여 출제 자격이 있는지 확인해줍니다
print(result)
# 결과를 출력해줍니다