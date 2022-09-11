# SWEA 2007
t = int(input())
for test in range(1, t + 1):
    sen = input()
    for i in range(1, 10):
        for j in range(0, 30, i):
            if sen[:i] == sen[i: i + j]:
                print(f'#{test} {i}')
                break
    
# 문제에 구멍이 많아 정답 처리되는 조건에도 반례가 많이 존재할 수 있었음.