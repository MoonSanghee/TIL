n = list(map(int, str(input())))
change = int(input())
dele = []
while change:
    for i in range(len(n)):
        num = n[i::]
        if n[i] != max(num):
            dele.append(n[i])
            n[i] = max(num)
            n = n[:i:] + num.remove(max(num))

# print(n)

n = [1, 3, 2, 3, 1, 1]
# n.pop(3)
n -= [max(n)]
print(n)