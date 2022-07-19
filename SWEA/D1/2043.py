P, K = map(int, input().split())
if K > P:
    print(K - P + 1)
else:
    print(P - K + 1)