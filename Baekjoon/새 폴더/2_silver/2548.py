n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
# 수의 개수와 주어지는 수를 받고 정렬해줍니다.
print(numbers[(n - 1) // 2])
# 가운데 값을 확인하여 출력해줍니다.