n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 주어지는 예비소집 문제 결과를 받아줍니다
result = 0
# 결과를 담을 변수를 설정해줍니다
for a, b, c in arr:
    if a != -1:
        if b == c == -1:
            result += 1
        elif b >= a and c == -1:
            result += 1
        elif b >= a and c >= b:
            result += 1
# 1번 문제만 풀거나 1,2번 문제만 풀거나 1,2,3번 모두 푼 팀을 확인하여 결과를 갱신해줍니다
print(result)
# 결과를 출력해줍니다