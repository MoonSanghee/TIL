n=int(input())
# 물건의 수를 받아줍니다.
items = []
for i in range(n):
  items.append(int(input()))
items.sort(reverse = True)
# 물건의 가격을 받아 내림차순으로 정렬해줍니다.
result = sum(items)
for i in range(2, len(items), 3):
  result -= items[i]
# 모든 물건의 가격을 더하고 사은품으로 받을 수 있는 가격을 빼줍니다.
print(result)
# 지불해야하는 가격을 출력해줍니다.