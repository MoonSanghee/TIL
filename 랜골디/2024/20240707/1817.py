n, m = map(int, input().split())
# 책의 수와 박스에 담을수있는 최대 무게를 받아줍니다.
if n == 0:
    print(0)
    exit()
# 책이 0권이라면 박스가 필요없으므로 0을 출력하고 연산을 멈추어줍니다.
books = list(map(int, input().split()))
# 책이 존재한다면 책이 놓여있는 상태를 받아줍니다.
result = 0
weight = 0
# 박스와 현재 담긴 무게를 담을 변수를 설정해줍니다.
for i in books:
    if weight + i > m:
        result += 1
        weight = i
    else:
        weight += i
    # 책을 차례대로 확인하며 새 박스가 필요한지 현재 박스에 담을수있는지를 확인하고 표시해줍니다.

if weight:
    result += 1
# 마지막 박스를 추가해줍니다.
print(result)
# 필요한 박스의 수를 출력해줍니다.