month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
m, d = map(int, input().split())
cnt = d - 1
for i in range(m - 1):
    cnt += month[i]

print(day[cnt % 7])