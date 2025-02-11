N, D = map(int, input().split())
# 주어지는 격자의 크기와 뒤집는 방향을 받아줍니다
for _ in range(N):
    result = ""
    word = input()
    if D == 1:
        for i in word:
            if i == "d":
                result += "q"
            elif i == "q":
                result += "d"
            elif i == "b":
                result += "p"
            elif i == "p":
                result += "b"
    elif D == 2:
        for i in word:
            if i == "d":
                result += "b"
            elif i == "b":
                result += "d"
            elif i == "q":
                result += "p"
            elif i == "p":
                result += "q"
    # 각줄의 입력을 받아 뒤집는 방향에 맞춰 뒤집은 값을 담아줍니다
    print(result)
    # 결과를 출력해줍니다