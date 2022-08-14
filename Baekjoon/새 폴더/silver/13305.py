cities = int(input())
length = list(map(int, input().split()))
gas = list(map(int, input().split()))
price = gas[0]
result = 0
for i in range(len(length)):
    if price > gas[i]:
        price = gas[i]
    result += price * length[i]
print(result)