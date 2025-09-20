n = int(input())
time = 0
length = 5000
# 주어지는 기록의 개수를 받고 시간과 코드의 길이를 주어진 범위에서 가장 작은값과 큰 값으로 설정해줍니다
for _ in range(n):
    t, b = map(int, input().split())
    time = max(time, t)
    length = min(length, b)
# 시간과 길이를 갱신해줍니다
print(((time * length) % 7) + 1)
# 캐릭터의 번호를 출력해줍니다