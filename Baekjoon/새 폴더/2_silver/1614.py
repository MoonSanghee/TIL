n = int(input())
cnt = int(input())
# 디찬 손가락과 사용할 수 있는 횟수를 받아줍니다
if n == 1:
    print(cnt * 8)
elif n == 5:
    print(cnt * 8 + 4)
else:
    if cnt % 2:
        print(cnt * 4 + 5 - n)
    else:
        print(cnt * 4 + n - 1)
    # 각 조건에 따라 결과를 출력해줍니다