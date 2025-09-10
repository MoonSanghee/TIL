h, m = map(int, input().split())
# 시침과 분침의 각도를 받아줍니다
if (h % 30) * 12 == m:
    print("O")
else:
    print("X")
    # 시침과 분침이 정상인지 확인하여 결과를 출력해줍니다