n = int(input())
a, b = map(int, input().split())
# 치킨의 제한과 콜라, 맥주의 개수를 받아줍니다.
m = a // 2 + b
# 최대 먹을수있는 치킨을 받아줍니다.
print(min(n, m))
# 남은 치킨과 먹을수있는 치킨중 작은 값을 출력해줍니다.