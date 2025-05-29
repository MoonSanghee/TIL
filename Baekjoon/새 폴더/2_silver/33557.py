t = int(input())
# 테스트 케이가의 개수를 받아줍니다
for _ in range(t):
    a, b = input().split()
    c = int(a) * int(b)
    # 주어지는 두 수를 받고 곱을 구해줍니다

    if len(a) < len(b):
        a, b = b, a
        b = b.rjust(len(a), '1')
    elif len(a) > len(b):
        b = b.rjust(len(a), '1')
    # 두 수중 짧은 수의 앞에 길이의 차이만큼 1을 채워줍니다
    d = ''
    for i in range(len(a)):
        d += str(int(a[i]) * int(b[i]))
    # 각 자리수를 곱하여 나오는 값을 구하여줍니다
    if c == int(d):
        print(1)
    else:
        print(0)
    # 결과를 출력해줍니다