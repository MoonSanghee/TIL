n = int(input())
line = list(map(int, input().split()))
# 사람의 수와 현재 줄을 선 상태를 받아줍니다.
cnt = 0
for i in range(n):
    if line[i] != i + 1:
        cnt += 1
# 제자리에 서있지 않은 사람을 확인해줍니다.
print(cnt)
# 결과를 출력해줍니다.