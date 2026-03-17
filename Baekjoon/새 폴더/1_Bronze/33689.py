N = int(input())
# 대회 이름의 수를 받아줍니다
result = 0
# 결과를 담을 변수를 설정해줍니다
for _ in range(N):
    name = input()
    if name[0] == 'C':
        result += 1
# C로 시작하는 이름의 수를 찾아줍니다
print(result)
# 결과를 출력해줍니다