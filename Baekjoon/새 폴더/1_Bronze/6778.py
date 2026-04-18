antenna = int(input())
eyes = int(input())
# 더듬이와 눈의 수를 받아줍니다
if antenna >= 3 and eyes <= 4:
    print("TroyMartian")
if antenna <= 6 and eyes >= 2:
    print("VladSaturnian")
if antenna <= 2 and eyes <= 3:
    print("GraemeMercurian")
# 주어지는 조건에 부합하는 종족을 출력해줍니다