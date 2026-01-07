n = int(input())
# 출력할 영역의 크기를 받아줍니다
for i in range(5):
    for _ in range(n):
        if i != 4:
            print('@' * n)
        else:
            print('@' * n * 5)
        # 주어진 형식에 맞게 결과를 출력홰줍니다