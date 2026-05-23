check = []
for i in range(1, 1000):
    if i ** 2 > 1000:
        break
    if str(i) == str(i)[::-1]:
        character = str(i ** 2)
        if character == character[::-1]:
            check.append(i ** 2)
# 주어진 범위 안의 제곱수중 펠린드롬을 이루는것을 모두 찾아줍니다
T = int(input())
# 테스트 케이스의 수를 받아줍니다
for t in range(T):
    A, B = map(int, input().split())
    # 범위를 받아줍니다
    result = 0
    for i in check:
        if A<= i <= B:
            result += 1
    
    print(f'#{t + 1} {result}')
    # 주어진 형식대로 결과를 출력해줍니다