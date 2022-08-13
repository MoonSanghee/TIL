test = int(input())
for t in range(test):
    n, m = list(map(int, input().split()))
    def fact(x):
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result
    answer = fact(m) / (fact(n)*fact(m - n))
    print(int(answer))