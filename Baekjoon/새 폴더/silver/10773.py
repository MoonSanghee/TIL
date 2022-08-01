input_times = int(input())

result = []

for _ in range(input_times):
    a = int(input())
    
    if a == 0:
        result.pop()
    else:
        result.append(a)

print(sum(result))