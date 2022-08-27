price = int(input())

kind = int(input())
sum = 0
for i in range(kind):
    each_price, cnt = map(int, input().split())
    sum += each_price * cnt

if sum == price:
    print('Yes')
else:
    print('No')