soomi = list(map(int, input().split()))
made = list(map(int, input().split()))
q = int(input())
# 주어지는 변수들을 받아줍니다
cookie = 0
# 만든 쿠키의 누적 개수를 담을 변수를 설정해줍니다
for _ in range(q):
    query = list(map(int, input().split()))
    # 주어지는 쿼리를 받아줍니다
    if query[0] == 1:
        for i in range(4):
            if soomi[i] < made[i] * query[1]:
                print("Hello, siumii")
                break
        else:
            cookie += query[1]
            print(cookie)
            for i in range(4):
                soomi[i] -= made[i] * query[1]
    elif query[0] == 2:
        soomi[0] += query[1]
        print(soomi[0])
    elif query[0] == 3:
        soomi[1] += query[1]
        print(soomi[1])
    elif query[0] == 4:
        soomi[2] += query[1]
        print(soomi[2])
    else:
        soomi[3] += query[1]
        print(soomi[3])
    # 쿼리의 실행 결과를 출력해줍니다