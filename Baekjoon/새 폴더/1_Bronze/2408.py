n = int(input())
# 주어지는 연산자의 수를 받아줍니다
line = input()

for _ in range(n - 1):
    line += input()
    line += input()
line = line.replace("/", "//")
# 주어지는 수식을 받고 나누기 기호를 몫만 받도록 수정해줍니다
print(eval(line))
# eval함수를 이용해 문자열을 계산한 결과를 출력해줍니다