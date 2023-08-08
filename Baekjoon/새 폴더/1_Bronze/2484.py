n = int(input())
# 참가하는 사람의 수를 받아줍니다.
best = 0
# 상금 최고액을 기록할 변수를 정해줍니다.
for _ in range(n):
    dice = sorted(list(map(int, input().split())))
    # 주사위 값을 리스트로 받아 정렬해줍니다.
    if len(set(dice)) == 1:
        price = 50000 + dice[0] * 5000
        # 리스트를 세트로 바꾸었을때 길이가 1이라면 4개의 눈이 같으므로 
        # 상금을 4개의 눈이 같은 경우로 계산하여줍니다.
    elif len(set(dice)) == 2:
        if dice[1] == dice[2]:
            price = dice[1] * 1000 + 10000
            # 리스트를 세트로 바꾸었을때 1번 인덱스와 2번 인덱스 값이 같다면
            # 3개의 눈이 같은 경우이므로 3개의 눈이 같은 경우로 상금을 계산해줍니다.
        else:
            price = dice[1] * 500 + dice[2] * 500 + 2000
            # 1번 인덱스와 2번 인덱스 값이 다르다면 2개씩 두 쌍의 조합으로 상금을 계산해줍니다.
    elif len(set(dice)) == 4:
        price = dice[3] * 100
        # 4개의 눈이 다 다르다면 가장 뒤에 위치한 눈이 가장 크므로 그 값에 100을 곱한값이 상금으로 설정해줍니다.
    else:
        for i in range(3):
            if dice[i] == dice[i + 1]:
                price = 1000 + 100 *dice[i]
                # 그 외의 경우 2개 짝이 한 쌍인 경우이므로 같은 눈을 찾아 상금을 계산해줍니다.
    best = max(best, price)
    # 최고액과 상금을 비교하여 최고액을 갱신해줍니다.

print(best)
# 최고액에 저장된 값을 출력해줍니다.