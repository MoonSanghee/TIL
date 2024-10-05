n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
# 수열의 길이와 수열을 받고 정렬해줍니다
print(*numbers)
# 수열을 출력해줍니다.