numbers = [0] * 500001
# 수의 개수를 담을 리스트를 만들어줍니다,
n = int(input())
# 수의 개수를 받아줍니다.
arr = map(int,input().split())
# 수열을 받아줍니다.
for k in arr:
    numbers[k] += 1
    # 수의 개수를 표시해줍니다.
print(max(numbers))
# 가장 많이 나온 수가 최소 만들어야하는 탑의 개수이므로 가장 많이 나온 수를 출력해줍니다