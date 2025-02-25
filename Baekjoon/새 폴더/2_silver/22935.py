t = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(t):
    n = int(input())
    n %= 28
    # 15까지 늘어났다가 1이될때까지 줄어드므로 28씩 패턴이 반복됩니다
    if n == 0:n=2
    elif n > 15:n=30-n
    # 28로 나누어 떨어질경우 2일 때와 같은 값을 가지고 16 이상의 경우 1씩 줄어드므로 30에서 뺀 값으로 갱신해줍니다
    number = bin(n)[2:].zfill(4)
    result = ''
    # 수를 2진수로 전환하고 4자리가 안 되면 0으로 체워줍니다
    for i in number:
        if i == '0':result+='V'
        else:result+='딸기'
    print(result)
    # 결과를 출력해줍니다