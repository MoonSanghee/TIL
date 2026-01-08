n = int(input())
# 영역의 크기를 받아줍니다
for i in range(5):
    for _ in range(n):
        if i != 0:
            print('@' * n)
        else:
            print('@' * n * 5)
    # 영역의 크기에 맞게 요구받은 모양을 출력해줍니다