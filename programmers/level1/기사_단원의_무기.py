def solution(number, limit, power):
    cnt = [0 for _ in range(number + 1)]
    # 각 수의 약수의 개수를 담을 변수를 설정해줍니다
    for i in range(number):
        i += 1
        for j in range(i, number + 1, i):
            cnt[j] += 1
    # 주어지는 정수 이하의 모든 정수를 순회하며 각 정수의 배수마다 약수의 개수를 1씩 더해줍니다
    for i in range(number + 1):
        if cnt[i] > limit:
            cnt[i] = power
    # 약수의 개수가 리미트보다 많다면 주어진 수로 값을 갱신해줍니다
    return sum(cnt)
    # 결과를 출력해줍니다