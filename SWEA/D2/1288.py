T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n = int(input())
    # 처음 주어지는 수를 받아줍니다
    number = n
    passed = set()
    cnt = 0
    # 주어지는 수의 몇배수를 확인중인지 담을 변수를 설정해줍니다
    while len(passed) < 10:
        cnt += 1
        word = str(n * cnt)
        passed.update(set(list(word)))
    # 배수를 갱신하여 각 자리수를 세트에 추가해줍니다
    print(f'#{t + 1} {number * cnt}')
    # 결과를 주어진 형식에 맞춰 출력해줍니다