n = int(input())
k = input()
result = 0
# 수가 몇자리인지와 수를 받고 홀짝의 개수를 담을 변수를 설정합니다
for i in k:
    if int(i) % 2 == 1:
        result += 1
    else:
        result -= 1
# 자리수를 확인해 홀수라면 결과를 더하고 짝수라면 빼줍니다
if result > 0:
    print(1)
elif result == 0:
    print(-1)
else:
    print(0)
# 결과를 확인하여 주어진 조건대로 출력해줍니다