t = int(input())
# 입력 횟수를 받아줍니다.
for tc in range(t):
    n = int(input())
    # 정수를 받아줍니다.
    new = bin(n)[::-1]
    # 입력받은 정수를 bin 함수를 통해 이진수로 전환하고 뒤집어줍니다.
    one = []
    for i in range(len(new)):
        # 2진수로 전환하여 뒤집은 수를 순회하며 1인 자리를 리스트에 담아줍니다.
        if new[i] == '1':
            one.append(i)
    print(*one)
    # 리스트에 담긴 1의 자리들을 출력해줍니다.