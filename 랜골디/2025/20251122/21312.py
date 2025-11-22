A, B, C = map(int, input().split())
result = 1
# 주어지는 세 음료와 결과를 담을 변수를 설정해줍니다
drink = [A, B, C]
# 세 음료를 리스트에 담아줍니다
for i in drink:
    if i % 2:
        result *= i
# 번호가 홀수인 음료를 결과에 곱해줍니다
if result == 1 and 1 not in drink:
    for i in drink:
        result *= i
# 결과가 최초 설정해놓은 상태이고 고유번호가 1인 칵테일이 없으면 모든 칵테일이 짝수이므로 모든 칵테일의 번호를 곱해줍니다
print(result)
# 결과를 출력해줍니다