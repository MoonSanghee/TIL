n, m = map(int, input().split())
# 전체 지폐와 묶음의 단위를 확인해줍니다.
cnt = 0
while n:
    cnt += n
    n //= m
# 묶음이 되는지 확인하지 않은 뭉치를 확인하며 묶음을 만드는것을 반복합니다.
print(cnt)
# 세어야하는 횟수를 출력해줍니다.