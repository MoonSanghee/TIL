y, m, d = list(map(int, input().split('-')))
n = int(input())
# 주어지는 날짜와 지나가는 날의 수를 받아줍니다.
d += n
m += (d - 1) // 30
d = (d - 1) % 30 + 1
y += (m - 1) // 12
m = (m - 1) % 12 + 1
# 일수에 주어지는 날을 더하고 월, 연도 순으로 바뀌는값을 확인해줍니다.
day = str(d)
month = str(m)
year = str(y)
# 연도, 달, 날을 문자열로 변환해줍니다.
if len(month) == 1:
    month = '0' + month
if len(day) == 1:
    day = '0' + day
# 연도는 1000에서 3000사이가 주어지므로 상관없지만 날짜나 달은 한자리수의 경우 0을 앞에 더해줍니다.
print(f'{year}-{month}-{day}')
# 주어진 형식에 맞추어 출력해줍니다.