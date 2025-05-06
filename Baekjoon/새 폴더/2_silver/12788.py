n = int(input())
m, k = map(int, input().split())
# CTP 회원수와 참가 팀의 수, 팀을 구성하는데 필요한 팀원의 수를 받아줍니다
pens = sorted(list(map(int, input().split())), reverse = True)
cnt = 0
# 최대한 적은 회원들에게 펜을 빌리려하므로 회원들이 가진 펜의 수를 내림차순으로 정렬하고 빌린 펜의 수를 담을 변수를 설정해줍니다
for i in range(n):
    cnt += pens[i]
    if cnt >= m * k:
        print(i + 1)
        break
    # 각 회원에게 빌릴수 있는 펜의 수를 더하고 필요한 펜의 수가 충족되면 반복을 멈추고 몇 명에게 빌렸는지 출력해줍니다
else:
    print("STRESS")
    # 모든 펜을 빌려도 펜이 부족하다면 주어진 값을 출력해줍니다