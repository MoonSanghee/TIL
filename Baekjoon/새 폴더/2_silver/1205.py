n, new, p = map(int, input().split())
# 기록된 점수의 개수와 새로 기록될 점수, 기록할 수 있는 점수의 개수를 받아줍니다.

if not n:
    print(1)
    # 기록된 점수가 없다면 1을 출력해주고
else:
    scored = list(map(int, input().split()))
    # 기록된 점수가 있다면 scored라는 이름으로 점수들을 리스트 형태로 받습니다.
    if n == p and scored[-1] >= new:
        print(-1)
        # 기록된 점수와 기록할 수 있는 점수의 개수가 같고 가작 작은 점수가
        # 새로 기록한 점수보다 크거나 같다면 -1을 출력하여줍니다.
    else:
        result = n + 1
        # 결과를 n + 1로 설정해줍니다.
        for i in range(n):
            # 기록된 점수를 순회하며
            if scored[i] <= new:
                # 기록된 점수가 새로 기록한 점수보다 같거나 작다면
                result = i + 1
                break
                # 순위를 갱신하고 반복을 멈추어줍니다.
        print(result)
        # result에 저장된 값을 출력해줍니다.