m,n = map(int, input().split())
# 두 수를 받아줍니다
result = ''
# 결과를 담을 변수를 설정해줍니다
while True:
    if m == 0:
        break
    x = m % n
    if x < 10:
        result += str(x)
    elif x == 10:
        result += 'A'
    elif x == 11:
        result += 'B'
    elif x == 12:
        result += 'C'
    elif x == 13:
        result += 'D'
    elif x == 14:
        result += 'E'
    elif x == 15:
        result += 'F'
    m //= n
    # 주어진 n으로 나눈 나머지를 차례대로 담아줍니다
if result:
    print(result[::-1])
else:
    print(0)
# 문자열이 비어있다면 0을 출력해주고 아니면 문자열을 뒤집어 출력해줍니다