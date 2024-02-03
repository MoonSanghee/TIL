n, r, c = map(int,input().split())
# 영역의 크기와 당근이 심어진 위치를 받아줍니다.
if (r + c) % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            print("v." * (n // 2) + 'v' * (n % 2))
        else:
            print(".v" * (n // 2) + '.' * (n % 2))
            
else:
    for i in range(n):
        if i % 2 == 1:
            print("v." * (n // 2) + 'v' * (n % 2))
        else:
            print(".v" * (n // 2) + '.' * (n % 2))

# 당근이 심어진 x, y좌표의 합이 짝수인지 홀수인지 확인하여 합을 2로 나눈 나머지가 같은 장소마다 당근을 심고 결과를 출력해줍니다.