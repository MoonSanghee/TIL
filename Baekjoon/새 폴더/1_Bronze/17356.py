a, b = map(int, input().split())
m = (b - a) / 400
answer = 1 / (1 + 10 ** m)
print(answer)
# 주어지는 두 정수를 받고 변수로 대입하여 결과값을 출력해줍니다