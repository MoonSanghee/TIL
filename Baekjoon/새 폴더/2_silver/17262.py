n = int(input())
# 팬의 수를 받아줍니다
start = 0
end = 100000
# 주어진 시간 범위의 최소와 최대 값으로 욱제가 학교에 머물러야하는 시간을 설정해줍니다
for _ in range(n):
    a, b = map(int, input().split())
    start = max(start, a)
    end = min(end, b)
# 팬이 머무는 시간을 받고 학교에 머물러야하는 시작 시간과 떠나는 시간을 갱신해줍니다
print(max(0, start - end))
# 욱제가 학교에 머물러야하는 시간을 출력해줍니다