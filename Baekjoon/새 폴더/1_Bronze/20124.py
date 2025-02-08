n = int(input())
score = 0
names = []
# 사람의 수를 받고 최다 득점을 담을 변수와 최다 득점자들의 이름을 담을 변수를 설정해줍니다

for _ in range(n):
    name, point = input().split()
    if int(point) > score:
        score = int(point)
        names = [name]
    elif int(point) == score:
        names.append(name)
    # 입력받은 이름과 득점을 이전 최다득점과 비교해 득점이 갱신되면 리스트를 새로 만들어주고
    # 공동 최다득점이라면 이름만 넣어줍니다

names.sort()
# 이름을 정렬해줍니다
print(names[0])
# 결과를 출력해줍니다