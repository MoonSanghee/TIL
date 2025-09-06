n = int(input())

for i in range(5):
    for _ in range(n):
        if i % 2 == 1:
            print("@" * 5 * n)
        else:
            print("@" * n + "   " * n + "@" * n)
# 상자의 크기를 받고 모양에 맞게 출력하여줍니다