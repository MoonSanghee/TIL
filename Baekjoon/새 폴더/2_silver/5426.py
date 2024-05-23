t = int(input())

for _ in range(t):
    massage = input()
    n = int(len(massage) ** 0.5)

    new = ''
    for i in range(n, 0, -1):
        for j in range(i, n * n + 1, n):
            new += massage[j - 1]
    
    print(new)