tc = int(input())
for t in range(tc):
    days = int(input())
    stock = list(map(int, input().split()))
    value=0
    max=0
    for i in range(days-1,-1,-1):
        if(stock[i] > max):
            max = stock[i]
        else:
            value+=max-stock[i]
    print(value)
    # 매일의 주가를 역순으로 탐색하여 가장 이전 날 가격이 현재까지 최고가보다 크면 그
    # 차액만큼 이득을 볼 수 있고 아니면 차액을 갱신해주고 이득을 못 보는것으로 확인하면 최대 수익을 확인 할 수 있습니다.