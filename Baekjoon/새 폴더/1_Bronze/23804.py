n = int(input())
# 출력할 영역의 크기를 받아줍니다
for i in range(5):
    for _ in range(n):
        if i == 0 or i == 4:
            print('@' * n * 5)
        else:
            print('@' * n)
    # 몇번째 줄을 출력해야하는지 확인하여 주어진 형식에 맞게 출력해줍니다