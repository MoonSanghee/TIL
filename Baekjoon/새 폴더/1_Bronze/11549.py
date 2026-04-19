T = int(input())
answer = list(map(int, input().split()))
result = 0
# 주어지는 차의 종류와 참가자들의 정답을 받고 결과를 담을 변수를 설정해줍니다
for i in answer:
    if i == T:
        result += 1
# 정답을 맞춘 참가자수를 확인해줍니다
print(result)
# 결과를 출력해줍니다