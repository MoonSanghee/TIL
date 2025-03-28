n = int(input())
names = []
# 주어지는 이름의 수를 받고 후보자를 담을 변수를 설정해줍니다
for _ in range(n):
    name = input()
    if len(name) == 3:
        names.append(name)
    # 주어지는 이름이 3글자라면 후보자 목록에 넣어줍니다
names.sort()
print(names[0])
# 후보자들을 정렬하여 가장 앞의 이름을 출력해줍니다