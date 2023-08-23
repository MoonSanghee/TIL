e, f, c = map(int, input().split())
# 가진 빈 병의 수와 주운 빈 병의 수 교환에 필요한 병의 수를 받아줍니다.
bottle = e + f
# 가진 총 병의 수를 설정해줍니다.
cnt = 0
# 바꾼 병의 수를 저장할 변수를 설정해줍니다.
while True:
    if bottle < c:
        break
    # 가진 빈병으로 교환할 수 없다면 반복을 멈추어줍니다.
    else:
        cnt += bottle // c
        bottle = bottle // c + bottle % c
    # 가진 빈 병으로 음료로 교환이 가능하면
    # cnt에 교환한 음료의 수를 더해주고 가진 병의 수를 
    # 교환한 병의 수와 교환하지 못하고 남은 병의 수로 갱신하여줍니다.
print(cnt)
# 총 교환하여 받은 병의 수를 출력하여줍니다.