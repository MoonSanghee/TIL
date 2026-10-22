T = int(input())

for tc in range(T):
    a, b = map(int, input().split())
    words = [input() for _ in range(a)]
    result = 0

    for _ in range(b):
        i = input()
        for j in words:
            if i == j[:len(i)]:
                result += 1
                break
    
    print(f'#{tc + 1} {result}')