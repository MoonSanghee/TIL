numbers = list(input().split())
a = input()
result = 0
# 주어지는 변수들을 받고 결과를 담을 변수를 설정해줍니다
for n in numbers:
    if n != a and n[:len(a)] == a:
        result += 1
# 주어진 조건에 맞는 번호의 수를 찾아줍니다
print(result)
# 결과를 출력해줍니다