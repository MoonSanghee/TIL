n = int(input())
# 출력하려는 영역의 크기를 받아줍니다
for i in range(5):
    for _ in range(n):
        if i == 0 or i == 2:
            print("@" * n * 5)
        else:
            print("@" * n)
    # 요청받은 모양을 출력해줍니다