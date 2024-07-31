junsung, ikjun = map(int, input().split())
finger = (0, 2, 5)
# 두사람의 편 손가락을 받고 손가락을 받아줍니다.
if junsung in finger and ikjun not in finger:
    print(">")
elif junsung not in finger and ikjun in finger:
    print("<")
# 한 쪽이 가위바위보 중에 내고 다른 한 사람이 내지않으면 낸쪽이 이깁니다.
elif junsung in finger and ikjun in finger:
    if (finger.index(junsung) + 1) % 3 == finger.index(ikjun):
        print(">")
    elif (finger.index(ikjun) + 1) % 3 == finger.index(junsung):
        print("<")
    else:
        print("=")
    # 둘 다 유효한것을 냈다면 결과를 확인해야합니다.
else:
    print("=")
# 둘 다 유효하지 않은 것을 냈다면 무승부입니다.