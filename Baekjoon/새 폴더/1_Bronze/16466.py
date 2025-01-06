n = int(input())
prices = sorted(list(map(int, input().split())))
# 팔린 티켓의 수와 티켓 번호들을 받고 티켓 번호를 정렬해줍니다
for i in range(n):
    if prices[i] != i + 1:
        print(i + 1)
        break
else:
    print(n + 1)
# n개의 티켓을 확인하며 살수있는 번호가 나왔다면 출력하고 순환을 멈추어주고 순환이 끝났다면 다음 번호를 출력해줍니다