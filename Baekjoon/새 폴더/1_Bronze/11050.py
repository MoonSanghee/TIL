n, k = map(int, input().split())
t = n - k
# 이항 계수를 구하기 위해서 n팩토리얼에 k팩토리얼과 (n - k) 팩토리얼을 나눈값을 구하여야 합니다.
# n - k를 t로 설정해줍니다.
result = 1
while n > k:
    result *= n
    n -= 1
# k만큼 다시 나눌것이기 때문에 n이 k가 될때까지 1씩 빼주면 결과에 곱하여줍니다.
while t:
    result //= t
    t -= 1
    # result에 저장된 값을 t로 나누어주고 1씩 빼면서 t가 0이 될때까지 반복합니다.
print(result)
# result에 저장된 값을 출력합니다.