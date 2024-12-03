t = int(input())
# 테스트 케이스의 수를 받아줍니다
for tc in range(t):
    n = int(input())
    candy = list(map(int, input().split()))
    cnt = 0
    # 아이의 수와 사탕을 몇개씩 가지고있는지를 받고 순환을 담을 변수를 설정해줍니다
    for i in range(n):
        if candy[i] % 2 == 1:
            candy[i] += 1
    # 사탕을 홀수개 가지고 있는 아이가 있다면 짝수개로 맞추어줍니다
    while len(set(candy)) != 1:
        # 사탕의 개수가 다른 아이들이 있다면 순환을 해줍니다
        cnt += 1

        add = [candy[-1] // 2]
        candy[-1] //= 2
        # 사탕을 몇개씩 옮길지 담을 변수를 만들고 가장 오른쪽 아이 사탕의 반을 담아줍니다
        for i in range(n - 1):
            add.append(candy[i] // 2)
            candy[i] //= 2
            # 가장 오른쪽 아이의 전까지 차례대로 사탕을 반씩 더할 사탕 리스트에 담아줍니다
        
        for i in range(n):
            candy[i] += add[i]
            if candy[i] % 2 == 1:
                candy[i] += 1
            # 아이들이 받을 사탕을 더해주고 홀수라면 1을 더해줍니다
    
    print(cnt)
    # 몇번의 순환을 거쳐 모두 같은 사탕을 가지게 되었는지 출력해줍니다