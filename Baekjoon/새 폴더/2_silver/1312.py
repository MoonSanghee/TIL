a, b, n = map(int, input().split())
a %= b
for _ in range(n - 1):
    a = (a * 10) % b
result = (a*10)//b
print(result)
# 나누어 지는 수에 10의 n 승을 곱해주고 b로 나누어진 몫의 가장 마지막 자리값을 출력했습니다. -> 시간초과
# a를 b로 나눈 나머지를 다시 a라하고 이에 10을 곱하여 b로 나눈는것을 n-1번 반복하여 
# 마지막 나눗셈의 몫을 출력함 -> 찾아본 해결 방법