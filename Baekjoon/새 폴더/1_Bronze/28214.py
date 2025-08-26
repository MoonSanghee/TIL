n, k, p = map(int, input().split())
bread = list(map(int, input().split()))
# 주어지는 변수들을 받아줍니다
result = 0
# 팔 수 있는 묶음의 수를 담을 변수를 받아줍니다
for i in range(n):
    cnt = 0
    # 크림이 안 들어있는 빵의 수를 담을 변수를 설정해줍니다
    for j in range(k):
        if bread[i * k + j] == 0:
            cnt += 1
            if cnt == p:
                break
    else:
        result += 1
    # 묶음 단위로 순회하며 빵에 크림이 안 들었다면 값을 갱신하고 기준에 도달하였다면 다음 묶음을 확인하여주고
    # 묶음을 다 확인했을 때 기준에 충족한다면 결과값을 갱신해줍니다

print(result)
# 결과를 출력해줍니다