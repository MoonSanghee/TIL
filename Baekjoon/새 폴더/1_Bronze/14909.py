numbers = list(map(int, input().split()))
result = 0
# 주어지는 수열과 양수가 몇개인지 담을 변수를 설정해줍니다
for i in numbers:
    if i > 0:
        result += 1
# 수열을 순회하며 양수를 확인해줍니다
print(result)
# 결과를 출력해줍니다