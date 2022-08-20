test = int(input())
for t in range(1, test + 1):
    numbers = list(map(int, input().split()))
    for i in range(5):
        if numbers[i] < 40:
            numbers[i] = 40
    print(f'#{t} {sum(numbers)//5}')