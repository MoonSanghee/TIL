ml, mr, tl, tr = input().split()
ms = (ml, mr)
tk = (tl, tr)
# 두 사람이 낸 손의 상태를 받아줍니다.
hand = "RSP"

if ml != mr and tl != tr:
    print("?")
# 둘 다 다른 손을 냈다면 결과를 알수없습니다.
elif ml == mr and tl != tr:
    if hand[hand.index(ml) - 1] in tk:
        print("TK")
    else:
        print("?")
# 민성이만 같은 손을 냈다면 태경이가 이기는지 확인하여 결과를 출력해줍니다.
elif ml != mr and tl == tr:
    if hand[hand.index(tl) - 1] in ms:
        print("MS")
    else:
        print("?")
# 태경이만 같은 손을 냈다면 민성이가 이기는지 확인하여 결과를 출력해줍니다.
else:
    if hand[hand.index(ml) - 1] == tl:
        print("TK")
    elif ml == tl:
        print("?")
    else:
        print("MS")
# 둘 다 같은 손을 낸 경우 결과를 확인하고 출력해줍니다.