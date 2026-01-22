import sys
input = sys.stdin.readline

q = int(input())
# 주어지는 수의 개수를 받아줍니다
check = []
for i in range(32):
    check.append(2 ** i)
# 2의 32제곱 미만의 거듭제곱들을 리스트에 담아줍니다
for _ in range(q):
    a = int(input())
    if a in check:
        print(1)
    else:
        print(0)
    # 주어지는 수가 2의 거듭제곱인지 확인하여 결과를 출력하여줍니다