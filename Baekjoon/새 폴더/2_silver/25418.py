a, k = map(int, input().split())
cnt = 0
# a와 k를 받고 연산을 실행한 수를 담을 변수를 설정해줍니다.
while True:
    if a == k:
        print(cnt)
        break
    # a와 k가 같아지면 연산을 멈추고 실행한 연산의 횟수를 출력해줍니다.
    if k % 2 == 0 and k >= a * 2:
        k = int(k/2)
        # k가 짝수이고 a이상이라면 2로 나누어주고
    else:
        k -= 1
        # 아니라면 1을 빼줍니다
    cnt += 1
    # 연산을 실행하였음을 표시해줍니다.