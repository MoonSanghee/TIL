t = int(input())
# 카드 번호를 몇 개 받는지 확인해줍니다.
for _ in range(t):
    n = input()
    # 카드 번호를 받아줍니다.
    new = 0
    # 모든 자리수를 합할 변수를 정해줍니다.
    for i in range(len(n)):
        if i % 2 == 0:
            if int(n[i]) * 2 >= 10:
                new += (int(n[i]) * 2) // 10 + (int(n[i]) * 2) % 10
            else:
                new += int(n[i]) * 2
            # 짝수라면 2를 곱하고 10이상인지 확인하는 과정을 추가하여줍니다.
        else:
            new += int(n[i])
            # 홀수라면 그냥 자릿수를 더해줍니다.
        
    if new % 10:
        print('F')
    else:
        print('T')
        # 유효한지 결과를 출력해줍니다.