import datetime
date, target = input().split()
yy, mm, dd = map(int, date.split('-'))
target = int(target) - 1
# 주어지는 변수들을 입력받아줍니다
dday = datetime.datetime(yy, mm, dd)
dday = dday + datetime.timedelta(days = target)
# 파이썬 내장함수를 이용하여 주어지는 날짜를 데이트타임으로 변환하여 목표 일수를 더해줍니다
print(dday.strftime("%Y-%m-%d"))
# 주어진 형식에 맞게 출력해줍니다