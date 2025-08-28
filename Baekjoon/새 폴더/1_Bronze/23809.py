n = int(input())

for i in range(5):
    for _ in range(n):
        if i == 0 or i == 4:
            print("@" * n + "   " * n + "@" * n)
        elif i == 1 or i == 3:
            print("@" * n + "  " * n + "@" * n)
        else:
            print("@@@" * n)
    # 주어지는 정수를 받아 알맞은 형태를 출력해줍니다