n = int(input())
# 몇 쌍을 확인할지 받아줍니다.
group = set()
group.add("ChongChong")
# set구조에 ChongChong을 넣어줍니다.
for _ in range(n):
    A, B = input().split()
    if A in group or B in group:
        group.add(A)
        group.add(B)
    # 각 쌍 중에 무지개 댄스를 추고있는 사람이 있다면 set에 추가해줍니다.

print(len(group))
# 무지개 댄스를 추고있는 사람의 수를 출력해줍니다.