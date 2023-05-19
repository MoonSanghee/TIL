l, p = map(int, input().split())
# 공간의 크기와 단위면적당 인원을 받아줍니다.

cnt = l * p
li = list(map(int, input().split()))
# 파티에 온 전체 사람수와 신문에 난 사람수를 받아줍니다.

for i in range(5):
    li[i] -= cnt
# 각 페이지마다 실제 온 사람의 수를 빼줍니다.
print(*li)
# 결과를 출력해줍니다.