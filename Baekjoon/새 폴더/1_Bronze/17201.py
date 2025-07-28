n = int(input())
magnets = input()
# 자석의 개수와 주어지는 형태를 받아줍니다
for i in range(n * 2 - 1):
    if magnets[i] == magnets[i + 1]:
        print("No")
        break
    # 자석이 밀어내는 형태가 있다면 No를 출력해줍니다
else:
    print("Yes")
    # 모두 밀어내지 않는다면 Yes를 출력해줍니다