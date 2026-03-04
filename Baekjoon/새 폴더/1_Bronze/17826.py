scores = list(map(int, input().split()))
hongik = int(input())
# 학생들의 점수와 홍익이의 점수를 받아줍니다
for i in range(50):
    if scores[i] == hongik:
        if i < 5:
            print('A+')
        elif i < 15:
            print('A0')
        elif i < 30:
            print('B+')
        elif i < 35:
            print('B0')
        elif i < 45:
            print('C+')
        elif i < 48:
            print('C0')
        else:
            print('F')
        break
        # 홍익이의 등수에 해당하는 학점을 출력해줍니다