total = [1]
for i in range(2, 101):
    total.append(total[-1] + i ** 2)
# 각 정사각형의 개수를 리스트에 담아줍니다
while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(total[n - 1])
    # 영역의 크기를 받아 마지막 입력이 아니라면 정사각형이 몇 개 들어가는지 출력해줍니다