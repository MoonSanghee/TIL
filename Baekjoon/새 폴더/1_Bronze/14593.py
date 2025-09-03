n = int(input())
# 참가자의 수를 받아줍니다
arr = [list(map(int, input().split())) + [i + 1] for i in range(n)]
arr.sort(key=lambda x : (-x[0], x[1], x[2]))
# 참가자의 기록과 번호를 받고 주어진 방식대로 정렬해줍니다
print(arr[0][3])
# 1등 참가자의 번호를 출력해줍니다