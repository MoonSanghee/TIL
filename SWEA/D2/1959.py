# import sys

# sys.stdin = open("1959_input.txt", "r")

T = int(input())
for i in range(T):
    Aj, Bj = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if Aj > Bj:
        a = Aj - Bj
        b2 = []
        for j in range(len(B)):
            b = []
            for k in range(a + 1):
                b.append(B[j]*A[j + k])
            b2.append(b)
    else:
        a = Bj - Aj
        b2 = []
        for j in range(len(A)):
            b = []
            for k in range(a + 1):
                b.append(A[j]*B[j + k])
            b2.append(b)
    b3 = []
    for l in range(len(b)):
        b4 = 0
        for m in range(len(b2)):
            b4 += b2[m][l]
        b3.append(b4)            
    print(f'#{i + 1}', end = ' ')
    print(max(b3))