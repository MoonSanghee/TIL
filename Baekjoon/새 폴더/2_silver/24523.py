import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# 수열의 길이와 주어지는 수열을 받아줍니다
result = []
start = 0
end = 0
# 결과를 담을 리시트와 같은 수의 구간을 담을 시작과 끝 자리를 변수에 설정해줍니다
while True:
    if end >= n:
        for i in range(start, end):
            result.append(-1)
        break
    # 마지막 인덱스가 수열의 범위를 벗어나면 남은 수만큼 -1을 결과에 담고 반복을 멈추어줍니다
    if arr[start] == arr[end]:
        end += 1
        # 수열에서 시작과 끝의 위치에 값이 같다면 끝의 범위를 1 늘려줍니다
    else:
        for i in range(start, end):
            result.append(end + 1)
        start = end
        end += 1
        # 수열의 시작과 끝의 위치에 값이 다르다면 같은 범위의 수만큼 달라지는 위치의 값을 넣고 시작과 끝 인덱스를 수정해줍니다

print(*result)
# 결과를 출력해줍니다