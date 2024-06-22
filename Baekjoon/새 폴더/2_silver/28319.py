n = int(input())
numbers = list(map(int, input().split()))
# 수의 개수와 수열을 받아줍니다.
odd = sum(numbers)
even = 0
for i in range(1, n, 2):
    even += numbers[i]
    odd -= numbers[i]
# 홀수와 짝수의 합을 구해줍니다.

if n == 3 and odd > even:
    print(-1)
    # 수가 3개이고 홀수의 합이 더 크다면 차이를 좁힐수 없으므로 -1을 출력해줍니다.
else:
    print(abs(odd - even))
    # 그 외의 경우 연속한 3수를 각 1씩 더해주면 홀수, 짝수의 합의 차를 1만큼씩 줄일수있으니 합의 차만큼 연산을 반복하면 됩니다