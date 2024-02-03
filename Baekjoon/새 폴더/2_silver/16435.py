n, l = map(int, input().split())
numbers = list(map(int, input().split()))
# 두 수와 수열을 받아줍니다.
numbers.sort()
# 수열을 오름차순으로 정렬해줍니다.
for i in numbers:
    if i <= l:
        l += 1
        # 수열을 차례로 돌며 과일을 먹을수 있다면 뱀의 길이를 1 증가시켜줍니다.
    else:
        break
        # 과일을 먹을수 없다면 순환을 멈추어줍니다.

print(l)
# 최대 길이를 출력해줍니다.