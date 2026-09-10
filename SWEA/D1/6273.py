scores = [(90, 80), (85, 75), (90, 100)]

for i in range(3):
    print(f'{i + 1}번 학생의 총점은 {sum(scores[i])}점이고, 평균은 {sum(scores[i]) / 2}입니다.')