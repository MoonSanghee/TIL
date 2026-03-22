n = int(input())
numbers = list(map(int, input().split()))
# 주어지는 수열의 길이와 수열을 받아줍니다
for i in range(1, n):
    if numbers[i] <= numbers[i - 1]:
        print(0)
        break
else:
    print(1)
# 수열이 오름차순인지 비내림차순인지 확인하여 결과를 출력해줍니다