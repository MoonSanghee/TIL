m, n = map(int, input().split())
snacks = list(map(int, input().split()))
# 과자를 받을 사람의 수와 과자의 수, 과자들의 길이를 받아줍니다.
start = 1
end = max(snacks)
# 최소 길이는 1, 과자를 붙일수 없으므로 최대 길이는 가장 긴 과자의 길이로 설정해줍니다.
answer = 0
# 답을 저장할 변수를 설정해줍니다.
while start <= end:
    # 범위가 유효하다면 계속 확인을 해줍니다.
    mid = (start + end) // 2
    cnt = 0
    # 범위의 중간값과 중간값으로 몇 개의 과자로 나뉘는지 담을 변수를 설정해줍니다.
    for i in snacks:
        cnt += i // mid
        # 과자를 순회하며 중위값으로 나눈 값을 cnt에 더해줍니다.
    if cnt >= m:
        answer = max(answer, mid)
        start = mid + 1
        # 과자가 충분히 많들어졌다면 answer의 값을 갱신해주고 start를 mid + 1로 갱신시켜 시작점을 당겨줍니다.
    else:
        end = mid - 1
        # 아니라면 범위의 끝나는 부분을 줄여줍니다.
        
print(answer)
# answer에 담긴 값을 출력해줍니다.