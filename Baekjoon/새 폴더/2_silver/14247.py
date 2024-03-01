# n일동안 n그루의 나무를 벱니다.
# 즉 모든 나무를 벨것이기 때문에 성장 속도가 빠른 나무일수록 나중에 배는것이 전체 길이가 더 길어지게됩니다.
n = int(input())
# n을 받아줍니다.
trees = list(map(int, input().split()))
growth = list(map(int, input().split()))
# 주어진 나무의 길이와 성장속도를 받아줍니다.
arr = []
for i in range(n):
    arr.append((trees[i], growth[i]))
# 리스트에 트리의 크기와 성장속도를 묶은 튜플 형태로 묶어 담아줍니다.
result = 0
# 전체 베어낸 나무 길이를 담을 변수를 설정합니다.
arr.sort(key = lambda x : x[1])
# 튜플을 담은 리스트를 성장속도 기준으로 오름차순 정렬을 실행해줍니다.
for i in range(n):
    result += arr[i][0] + arr[i][1] * i
# 결과에 주어진 나무의 크기와 i일동안 자란 크기를 더해줍니다.
print(result)
# 전체 베어낸 나무의 크기를 출력해줍니다.