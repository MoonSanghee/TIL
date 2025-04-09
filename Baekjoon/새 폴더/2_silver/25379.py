n = int(input())
numbers = list(map(int, input().split()))

odds = 0
evens = 0
sort_by_odd = 0
sort_by_even = 0
for i in range(n):
    if numbers[i] % 2:
        odds += 1
        sort_by_odd += evens
    else:
        sort_by_even += odds
        evens += 1

print(min(sort_by_even, sort_by_odd))