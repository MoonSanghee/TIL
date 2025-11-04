n = input()
length = len(n)
# 주어지는 수와 길이를 담아줍니다
result = 0
# 버튼을 누른 횟수를 담을 변수를 설정해줍니다
while True:
    n = int(n)
    n *= 2
    number = str(n)
    # 버튼을 누른 결과를 실행해줍니다
    if len(number) > length:
        print(result)
        break
    else:
        result += 1
    # 자리수가 바뀌었다면 버튼을 누른 횟수를 갱신하지않고 결과를 출력하고 바뀌지 않았다면 횟수를 갱신해줍니다