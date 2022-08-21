test = int(input())
numbers = []
for t in range(1, test + 1):
    num = int(input())
    while num >= 10:
        num = sum(list(map(int, str(num))))
    numbers.append(f'#{t} {num}')

for i in numbers:
    print(i)