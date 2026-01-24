from collections import deque

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
known = deque(numbers[1:])
# 사람의 수와 파티의 수를 받고 진실을 아는 사람을 덱에 넣어줍니다
checked =[]
parties = []
# 진실을 아는 사람이 속한 파티를 확인한 후 담아둘 리스트와 파티 정보들을 담을 리스트를 만들어줍니다
for _ in range(m):
    info = list(map(int, input().split()))
    party = [True, info[1:]]
    parties.append(party)
# 파티 정보를 받고 과장할 수 있다는 표시와 참가 인원 정보를 묶어 파티 리스트에 넣어줍니다
while known:
    checked.append(known.popleft())
    # 진실을 아는 사람을 꺼내 확인 리스트에 넣어줍니다
    for i in range(len(parties)):
        if parties[i][0] == True:
            # 과장을 할 수 있는 파티중에
            if checked[-1] in parties[i][1]:
                # 진실을 아는 사람이 포함되어있는지 확인해줍니다
                for j in parties[i][1]:
                    if j not in checked or j not in known:
                        known.append(j)
                # 진실을 아는 사람이 있다면 모두 진실을 알고있으므로 리스트에 넣어줍니다
                parties[i][0] = False
                # 과장할 수 없디고 수정해줍니다

result = 0

for i in range(m):
    if parties[i][0] == True:
        result += 1
# 과장할 수 있는 파티의 수를 확인해줍니다
print(result)
# 결과를 출력해줍니다