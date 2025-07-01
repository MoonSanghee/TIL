n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())
# 참가하는 사람의 수와 사이즈별 신청한 사람 수, 펜과 셔츠의 묶음단위를 받아줍니다
shirt = 0
for i in sizes:
    shirt += i // t
    if i % t != 0:
        shirt += 1
# 사이즈별로 필요한 묶음을 확인해줍니다
print(shirt)
print(n // p, n % p)
# 요구하는 셔츠의 묶음과 펜 묶음, 낱개 펜의 수를 차례대로 출력해줍니다