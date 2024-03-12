n, k = input().split()
# 사람의 수와 게임의 종류를 받아줍니다.
people = set()
for _ in range(int(n)):
    people.add(input())
# 중복을 제외한 사람을 받아줍니다.
if k == "Y":
    print(len(people))
elif k == "F":
    print(len(people) // 2)
else:
    print(len(people) // 3)
# 게임의 종류에 따라 2, 3, 4명의 사람이 필요하지만 임스와 함께 하므로 1, 2, 3명의 사람을 선정해야합니다.
# 주어진 사람들은 각 1번씩만 게임을 할 수 있으므로 사람의 수를 게임에 필요한 인원으로 나눈 몫을 확인해 출력해줍니다.