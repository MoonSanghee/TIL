import datetime
start = datetime.date(2014, 4, 2)
n = int(input())
# 주어진 시작일과 기념하려는 날을 받아줍니다
result = start + datetime.timedelta(days = n - 1)
print(result.strftime("%Y-%m-%d"))
# python의 datetime을 이용하여 결과를 출력해줍니다