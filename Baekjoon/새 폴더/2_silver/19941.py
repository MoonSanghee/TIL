n, k = map(int, input().split())
# 식탁의 크기와 먹을수 있는 범위를 받아줍니다.
table = list(input())
# 입력받은 형태를 리스트로 받아줍니다.
cnt = 0
# 몇 개 먹을수 있는지 담아줄 변수를 설정해줍니다.
for i in range(n):
    if table[i] == 'P':
        # 테이블의 범위 안에서 인덱스의 위치가 사람이라면
        for j in range(max(i - k, 0), min(i + k + 1, n)):
            # 뻣을수 있는 범위를 테이블 범위 안과 비교하여 확인하고
            if table[j] == 'H':
                table[j] = 0
                cnt += 1
                # 햄버거가 있다면 0으로 바꿔주고 1개를 먹었다고 표시해줍니다.
                break
print(cnt)
# cnt에 담긴 값을 출력해줍니다.