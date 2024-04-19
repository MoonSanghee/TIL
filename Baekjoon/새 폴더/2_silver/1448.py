import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort(reverse=True)
# 변의 수를 받고 제공되는 변을 모두 받아 내림차순으로 정렬해줍니다.
answer = -1

for i in range(n - 2):
    if numbers[i] < numbers[i + 1] + numbers[i + 2]:
        answer = numbers[i] + numbers[i + 1] + numbers[i + 2]
        break
# 연속된 세 수가 삼각형을 이룰수 있는지 확인해 값을 갱신해줍니다.
print(answer)
# 가장 큰 삼각형의 세 변 길이를 출력해줍니다.