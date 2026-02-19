n = int(input())
result = 0
# 주어지는 수를 받고 결과를 담을 변수를 설정해줍니다
for i in range(n):
    result += 1
    if '50' in str(i):
        result += 1
# 주어진 수까지 순회하며 50이 포함된 경우 한 번씩 더해줍니다
print(result)
# 결과를 출력해줍니다