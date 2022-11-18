tc = int(input())
# 정수가 입력되는 횟수를 tc에 저장
for t in range(tc):
    n = int(input())
    # n에 받은 정수 저장
    di = {}
    while n != 1:
        for i in range(2, n + 1):
            if n%i == 0:
            # 정수를 2부터 정수까지중에 나누어 약수를 확인
                if i in di:
                    di[i] += 1
                else:
                    di[i] = 1
                n //= i
                break
            # 약수가 처음 나온 수면 딕셔너리에 키 값으로 넣고 1이라는 밸류를 주고
            # 나왔던 수라면 밸류값을 1 증가시킴

    for i in di:
        print(i, di[i])
    # 딕셔너리를 순환하며 키, 밸류 값을 출력해주었습니다.