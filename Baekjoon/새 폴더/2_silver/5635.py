n = int(input())
# 사람의 수를 받아줍니다.
people = []
# 사람의 정보를 입력할 리스트를 만들어줍니다.
for _ in range(n):
    name, day, month, year = input().split()
    # 입력받는 정보를 이름, 일, 월, 년 순으로 받아줍니다.
    day, month, year = map(int, (day, month, year))
    # 일, 월, 년을 정수로 변화시켜줍니다.
    people.append((year, month, day, name))
    # 만들어둔 리스트에 년,월,일,이름을 튜플형태로 묶어 넣어줍니다.
people.sort()
# 리스트를 정렬하여줍니다.
print(people[-1][3])
print(people[0][3])
# 생일이 빠를수록 앞에 있으므로 마지막 사람의 이름과 첫 사람의 이름을 출력해줍니다.