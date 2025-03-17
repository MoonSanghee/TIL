n = int(input())
seats = [["."] * 20 for _ in range(10)]
# 주어진 좌석 크기의 2차원 리스트를 만들어줍니다
for _ in range(n):
    info = input()
    row, column = info[0], int(info[1:])
    seats[ord(row) - 65][column - 1] = "o"
# 예약한 좌석을 찾아 표시해줍니다
for s in seats:
    print("".join(s))
# 각 줄별로 출력해줍니다
