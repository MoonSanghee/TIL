a, b = map(int, input().split())
# 주어지는 두 사람의 펴진 손가락 수를 받아줍니다..
while True:
    b += a
    if b >= 5:
        print('yt')
        break
    # 용태부터 공격을 시작해 이겼는지 확인해줍니다.
    a += b
    if a >= 5:
        print('yj')
        break
    # 용태가 공격을 했는데 게임이 끝나지 않으면 유진이가 공격하고 이기는지 확인해줍니다.
    # 게임이 안 끝난다면 번갈아가면 공격을 반복해줍니다.