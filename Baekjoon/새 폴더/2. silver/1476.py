numbers = list(map(int, input().split()))

while len(set(numbers)) != 1:
    e,s,m = numbers
    donot = max(numbers)
    if e != donot:
        numbers[0] += 15
    if s != donot:
        numbers[1] += 28
    if m != donot:
        numbers[2] += 19
print(numbers[0])