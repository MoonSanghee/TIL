q = int(input())
# 주어지는 이벤트의 개수를 받아줍니다
cnt = 0
# 남은 문제의 수를 담을 변수를 설정해줍니다
for _ in range(q):
    x, y = map(int, input().split())
    if x == 1:
        cnt += y
        # 문제 포럼에 추가할경우 주어지는 문제의 개수를 더해주고
    else:
        cnt -= y
        if cnt < 0:
            print("Adios")
            break
        # 사용할 경우 문제가 부족하다면 주어진 방식대로 출력하고 반복을 멈추어줍니다
else:
    print("See you next month")
    # 반복이 멈추지 않았다면 주어진 값을 출력해줍니다