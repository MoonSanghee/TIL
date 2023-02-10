x, y = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 몇월 몇일인지 받아주고
for i in range(x - 1):
    y += month[i]
# 입력된 달의 전 달만큼의 일수를 받은 일에 더하고
d = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

print(d[(y%7)])
# 'SUN'-'SAT'까지 담긴 리스트에서 7로 나누어 남은 값의 인덱스자리 값을 출력해줍니다.