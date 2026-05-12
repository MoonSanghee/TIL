A, B = input().split()
# 두 사람이 낸것을 받아줍니다
if (A == '3' and B == '2') or (A == '2' and B == '1') or (A == '1' and B == '3'):
    print("A")
else:
    print("B")
# 비기는 경우가 없으므로 한 사람이 이기는 경우를 확인하고 나머지는 다른 사람이 이긴다고 출력해줍니다