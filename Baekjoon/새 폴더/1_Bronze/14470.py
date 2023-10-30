a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
# 5개의 입력값을 차례대로 받아줍니다.
if a < 0:
    # b는 무조건 양수이므로 a가 음수이면 얼어있는 고기를 녹이고 
    # b까지 도달하는 시간을 구해야하고
    print(abs(a) * c + d + b * e)
else:
    # a가 양수이면 b에서 a를 뺀 값에 e를 곱한 값을 출력해줍니다.
    print((b - a) * e)