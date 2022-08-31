n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)

g = [0, 0]
h = [0, numbers[0]]    
for i in range(1, n + 1):
