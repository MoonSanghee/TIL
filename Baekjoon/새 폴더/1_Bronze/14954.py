n = int(input())
check = [n]
# 주어지는 수를 받고 반복되고있는지 확인하기 위해 계산 결과를 모을 리스트를 만들어줍니다
def funtion(x):
    result = 0
    while x:
        result += (x % 10) ** 2
        x //= 10
    if result == 1:
        print("HAPPY")
        return 
    elif result in check:
        print("UNHAPPY")
        return 
    else:
        check.append(result)
        funtion(result)
    # 각 자리수의 제곱을 더하여 행복한수인지 반복되는지 확인될 때까지 재귀해줍니다
funtion(n)
# 함수를 실행시켜줍니다