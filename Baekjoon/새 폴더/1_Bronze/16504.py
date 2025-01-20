n = int(input())
# 종이의 크기를 받아줍니다
result = 0
for _ in range(n):
    result += sum(list(map(int, input().split())))
print(result)
# 1개의 칸이 될 때까지 접으므로 모든 칸의 수를 더해 출력해줍니다