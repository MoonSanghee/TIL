# 8-5 문제번호 4948

m = 1
while m != 0 :
    m = int(input())
    cnt = []
    for i in range(m + 1, 2 * m + 1):    
        if i == 1:
        #1은 소수가 아니므로 제외
            continue
        for j in range(2, int(i ** 0.5) + 1):
            # i의 제곱근까지 인수를 가지지 못하면 소수 일 수밖에 없다.
            # 범위는 정수여야 하므로 i ** 0.5를 정수형으로 출력시킨다.
            if i % j == 0:
                break
        else:
            cnt.append(i)
            #소수들을 cnt 리스트로 추가
    if m != 0:
        print(len(cnt))
    else:
        break