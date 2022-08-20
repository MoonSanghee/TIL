n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)
numbers = numbers[::-1]

def find(x):
    result = []
    point = numbers[0]
    
