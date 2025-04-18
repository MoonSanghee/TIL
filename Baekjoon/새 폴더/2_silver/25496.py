p, n = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cnt = 0
# 주어지는 현재 피로도와 제작할 장신구의 수를 받고
# 장신구를 제작하는데 필요한 피로도를 받아 오름차순으로 정렬해줍니다
# 장신구를 제작한 회수를 담을 변수를 설정해줍니다
for i in arr:
    if p < 200:
        p += i
        cnt += 1
    else:
        break
# 피로도가 제한을 넘기전까지 장신구를 제작하고 개수를 갱신해줍니다
print(cnt)
# 결과를 출력해줍니다