code = input()
# 주어지는 문자열을 받아줍니다
d = dict()
for i in range(1, 27):
    alpha = chr(64 + i)
    d[alpha] = i
# 각 알파벳에 1부터 26까지 숫자를 키, 밸류로 매칭하여 딕셔너리에 넣어줍니다
result = 0
# 결과를 담을 변수를 설정해줍니다
for i in range(len(code)):
    result *= 26
    result += d[code[i]]
# 자릿수가 바뀌면 이전까지 누적 값에 26을 곱하고 밸류값을 더해줍니다
print(result)
# 결과값을 출력해줍니다