n = int(input())
# 입력의 개수를 받아줍니다
for _ in range(n):
    code = input()
    score = 0
    # 입력을 받고 점수를 담을 변수를 설정해줍니다
    for i in code:
        if i == ' ':continue
        else:score += ord(i)-64
    if score == 100:print('PERFECT LIFE')
    else:print(score)
    # 각 자리를 확인하여 점수를 구한 뒤 주어진 조건에 맞게 출력해줍니다