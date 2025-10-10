while True:
    b, n = map(int, input().split())
    if b == n == 0:
        break
    # 주어지는 두 변수를 받아 마지막 입력인지 확인해줍니다
    i = 1
    while i ** n < b:
        i += 1
    # i의 n제곱이 b보다 작다면 i를 1씩 증가시켜줍니다
    if abs(i ** n - b) < abs((i - 1) ** n - b):
        print(i) 
    else: 
        print(i - 1)
    # i의 n제곱과 i - 1의 n제곱중 b에 가까운 수를 출력해줍니다