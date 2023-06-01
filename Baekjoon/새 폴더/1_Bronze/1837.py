p, k = map(int, input().split())
# 곱해서 나온 비밀번호와 하한을 정하여 줍니다.
bad = False
# 나쁜 암호가 아니라고 설정해줍니다.
for i in range(2, k):
    # 2부터 k까지 나누면서
    if not p % i:
        # 나누어떨어진다면
        bad = True
        num = i
        # 그 값을 하나의 값으로 가지는 나쁜수입니다.
        break

if bad:
    print('BAD', num)
else: 
    print('GOOD')
# 조건에 맞추어 출력해줍니다.