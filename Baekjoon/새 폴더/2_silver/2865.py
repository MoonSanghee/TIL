n, m, k = map(int, input().split())
numbers = [0] * n
# 주어지는 세 정수를 받고 각 참가자별로 최고득점이 가능한 점수를 담을 변수를 설정해줍니다
for _ in range(m):
    score = list(input().split())
    # 장르별 점수를 받아줍니다
    for i in range(0, n, 2):
        if numbers[int(score[i]) - 1] < float(score[i + 1]):
            numbers[int(score[i]) - 1] = float(score[i + 1])
            # 참가들의 점수를 확인해 이전 노래보다 좋은 점수를 받을수있다면 점수를 갱신해줍니다
numbers.sort(reverse = True)
result = round(sum(numbers[:k]), 1)
# 참가자들의 점수를 내림차순으로 정렬해 k명의 점수를 합하여 소수 1째짜리까지 반올림해줍니다
print(result)
# 결과를 출력해줍니다