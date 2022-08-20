# python 통과

import sys
M, N = map(int, sys.stdin.readline().split())

sqrt_ = int(N ** (1/2))

def p(n):
    if n == 1:
        return False
    else:
        for j in range(2, sqrt_ + 1):
            if n != j and not n % j:
                return False
            elif j == n:
                return True
        return True

for i in range(M, N + 1):
    if p(i):
        print(i)

#############################################

# python X pypy3 통과
 
import sys
M, N = map(int, sys.stdin.readline().split())

for i in range(M, N + 1):
    flag = True
    if i == 1:
        flag = False
    else:
        sqrt_ = int(N ** (1/2))
        for j in range(2, sqrt_ + 1):
            if i != j and not i % j:
                flag = False
                break
            elif j == i:
                break
    if flag:
        print(i)