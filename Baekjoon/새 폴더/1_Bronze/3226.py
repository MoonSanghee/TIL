n = int(input())
# 주어지는 통화회수를 받아줍니다.
result = 0

for _ in range(n):
    time, call = input().split()
    h, m = map(int, time.split(':'))
    # 전화건 시간과 통화시간을 받아줍니다.
    for _ in range(int(call)):
        if 7 <= h < 19:
            result += 10
        else:
            result += 5
        
        m += 1
        if m == 60:
            h += 1
            m = 0
    # 통화요금을 추가해줍니다.
print(result)
# 결과를 출력해줍니다.