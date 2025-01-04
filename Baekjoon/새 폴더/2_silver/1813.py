n = int(input())
counts = list(map(int, input().split()))
# 말의 개수와 정수의 개수를 받아줍니다
result = -1
# 결과를 담을 변수를 설정해줍니다
for i in range(n + 1):
    check = counts.count(i)
    if check == i:
        result = max(result, i)
    # i의 개수를 확인해 명제가 참이라면 결과를 갱신해줍니다
print(result)
# 결과값을 출력해줍니다