n = int(input())
# 주어지는 변수를 받아줍니다
for i in range(5):
    for _ in range(n):
        if i == 2 or i == 4:
            print("@" * (n * 5))
        else:
            print("@" * n + '   ' * n + "@" * n)
        # 주어진 형식대로 결과를 출력해줍니다