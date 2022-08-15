n, l = map(int, input().split())
po = list(map(int, input().split()))
po = sorted(po)
cnt = 0
start = 0
for i in po:
    if start == 0:
        cnt += 1
        start = i
    else:
        if i > start - 1 + l:
            start = i
            cnt += 1
print(cnt)
# 구멍이 난 곳을 정렬하여 끝까지 가면서 테이프를 붙이고 그 테이프의 범위 밖에 구멍이 있을 떄 또 테이프를 붙이는 식으로 
# 몇개의 테이프를 붙였는지 확인해주었다.