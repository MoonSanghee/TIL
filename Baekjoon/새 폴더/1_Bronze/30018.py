n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 자전거의 대수와 사용 전후 배치를 받아줍니다
result = 0
for i in range(n):
    result += abs(a[i] - b[i])
# 사용 전후 각 자리 자전거가 얼마나 이동했는지 확인해줍니다
print(result // 2)
# 한 번의 이동에 두 자리의 자전거를 1회씩 변경가능하므로 result의 값을 2로 나눠 출력해줍니다