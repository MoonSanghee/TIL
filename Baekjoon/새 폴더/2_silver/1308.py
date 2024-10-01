cnt = 0
# 시나리오 번호를 반복문 전에 선언해줍니다.
while True:
    cnt += 1
    # 시나리오 번호를 갱신하고 학생수를 받아줍니다.
    n = int(input())
    if n == 0:
        break
    # 학생수가 0이라면 작동을 멈추어줍니다.
    names = [input() for _ in range(n)]
    check = []
    # 학생의 이름을 차례대로 받고 귀걸이를 받아갔는지를 확인할 리스트를 만들어줍니다.

    for _ in range(n * 2 - 1):
        number, state = input().split()
        if number in check:
            check.remove(number)
        else:
            check.append(number)
    # 학생의 번호를 받고 리스트에 없다면 넣어주고 있다면 빼줍니다.
    print(f'{cnt} {names[int(check[0]) - 1]}')
    # 시나리오 번호와 남은 번호를 확인해 귀걸이를 받지 못한 학생의 이름을 출력해줍니다.