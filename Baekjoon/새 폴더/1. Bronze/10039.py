sum_ = 0
for i in range(5):
    number = int(input())
    if number < 40:
        number = 40
    sum_ += number

print(int(sum_ / 5))