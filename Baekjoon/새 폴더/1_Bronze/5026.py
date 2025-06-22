n = int(input())
# 주어지는 입력의 개수를 받아줍니다
for _ in range(n):
    command = input()
    # 입력을 받아줍니다
    if command == "P=NP":
        print("skipped")
        # 입력이 덧셈이 아니라면 주어진 출력을 해줍니다
    else:
        a, b = command.split("+")
        print(int(a) + int(b))
        # 입력이 덧셈이라면 주어진 수를 더한 결과를 출력해줍니다