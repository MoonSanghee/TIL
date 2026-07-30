T = int(input())
converter = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
# 테스트케이스의 개수를 받고 16진수의 두자리수를 담을 딕셔너리를 만들어줍니다
for t in range(T):
    n, number = input().split()
    result = ''
    # 수의 길이와 수를 받고 결과를 담을 변수를 설정해줍니다
    for i in number:
        if i in 'ABCDEF':
            i = converter[i]
        else:
            i = int(i)
        i = bin(i)[2:].zfill(4)
        result += i
    # 16진수의 각 자리값을 2진수로 변환하여 결과에 더해줍니다
    print(f'#{t + 1} {result}')
    # 주어진 양식에 맞춰 결과를 출력해줍니다