n, l, h = map(int, input().split())
points = sorted(list(map(int, input().split())))
print(sum(points[l:n-h])/(n-l-h))
# 주어지는 점수를 정렬하여 적은 순으로 l, 큰 순으로 h개를 빼고 평균을 구하여 출력해줍니다