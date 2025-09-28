n = int(input())
# 주어지는 정수를 받아줍니다
if n <= 21:
    number = 0
    for i in range(1, 8):
        number += i
        if number >= n:
            print(i)
            break
    # 영상을 보는데 7일 모두 사용할 필요가 없다면 몇 일이 필요한지 구하여 출력하고
else:
    if n % 7:
        print((n // 7) + 4)
    else:
        print((n // 7) + 3)
    # 7일 이상 필요하다면 첫 날 봐야하는 영상의 수를 출력해줍니다