N, b = map(int, input().split())
if N <= 2 ** (b + 1) - 1:
    print("yes")
else:
    print("no")
    # 주어지는 두 정수를 받고 압축이 가능한지 확인하여 결과를 출력해줍니다