n = int(input())

stack = []

result = 1

for _ in range(n):
    stack.append(int(input()))

m = stack[-1]

for i in range(len(stack)-1, -1, -1):
    if stack[i] > m:
        result += 1
        m = stack[i]

print(result)