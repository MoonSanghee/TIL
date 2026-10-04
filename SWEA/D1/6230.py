li = [88, 30, 61, 55, 95]

for i in range(5):
    if li[i] >= 60:
        print(f'{i + 1}번 학생은 {li[i]}점으로 합격입니다.')
    else:
        print(f'{i + 1}번 학생은 {li[i]}점으로 불합격입니다.')