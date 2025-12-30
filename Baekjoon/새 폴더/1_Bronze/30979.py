t = int(input())
n = int(input())
f = list(map(int, input().split()))
# 주어지는 변수들을 받아줍니다
if t > sum(f):
    print("Padaeng_i Cry")
else:
    print("Padaeng_i Happy")
# 결과를 출력해줍니다