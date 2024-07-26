n = int(input())
numbers = list(map(int, input().split()))
# 주어지는 수의 개수와 수들을 받아줍니다.
if n == 1 and numbers[0] == 0:
    print('YES')
    print(0)
    # 0만 주어지는경우 YES와 0을 출력해줍니다.
else:
    print("YES")
    print(111 * numbers[0])
    # 이외의경우 모든 수를 3번 나열한 수는 3의 배수이므로 주어진 수를 중복해 사용할수 있기 때문에 소수가 아닙니다.