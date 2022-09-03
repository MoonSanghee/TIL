numbers = [0, 1, 2, 4]
for i in range(4, 12):
    numbers.append(numbers[i - 1] + numbers[i - 2] + numbers[i - 3])
    
t = int(input())
for i in range(t):
    print(numbers[int(input())])