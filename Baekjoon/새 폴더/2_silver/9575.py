t = int(input())
# 테스트의 수를 받아줍니다.
for _ in range(t):
    a = int(input())
    A = list(map(int, input().split()))
    b = int(input())
    B = list(map(int, input().split()))
    c = int(input())
    C = list(map(int, input().split()))
    # 세 수열의 길이와 수열을 받아줍니다.
    numbers = set()
    # 행운의 수를 담을 set 자료형을 만들어줍니다.
    for i in A:
        for j in B:
            for k in C:
                number = str(i + j + k)
                for num in number:
                    if num != '5' and num != '8':
                        break
                else:
                    numbers.add(number)
                # 세 수열의 수를 순회하며 합이 행운의 수이면 set에 담아줍니다.

    print(len(numbers))
    # numbers의 길이를 출력해줍니다.