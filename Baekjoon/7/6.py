# 7-6 문제번호 2775

t = int(input())
for i in range(t):
    k = int(input())
    # 층 값을 입력
    n = int(input())
    # 호수를 입력
    k0 =[x for x in range(1, n + 1)]
    # 각 층을 리스트로 표현
    for k in range(k):
        #층을 순회하며
        for j in range(1, n):
            k0[j]  += k0[j - 1]
            #각 호수 값 입력
    print(k0[-1])
    #가장 마지막에 입력한 값을 출력