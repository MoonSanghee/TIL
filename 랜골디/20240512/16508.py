target = list(input())
d = dict()
for i in target:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
# 만들고자하는 단어를 받고 어떤 문자들로 이루어졌는지 확인해줍니다.
n = int(input())
books = []
for _ in range(n):
    price, name = input().split()
    books.append((int(price), name))
# 책이 몇권인지 받고 책의 제목과 가격을 튜플로 묶어 담아줍니다.
result = -1
# 원하는 단어를 만드는데 필요한 최소 비용을 담을 변수를 설정해줍니다.
books.sort(key = lambda x : x[0])
# 책을 가격의 오름차순으로 정렬해줍니다.

def find(num, title, price):
    # 몇번째 책의 정보가 추가되었는지 획득한 문자들은 어떤것들이 있는지 가격은 얼마인지 받아줍니다.
    global result
    flag = True
    for i in d:
        if title.count(i) < d[i]:
            flag = False
            break
    # 딕셔너리의 모든 문자를 확인해 다 가지고있다면 단어를 만들수 있다고 표시해줍니다.
    if flag:
        if result == -1:
            result = price
        else:
            result = min(result, price)
        return
    # 단어를 만들었다면 기존 가격을 확인하고 값을 갱신한후 연산을 멈추어줍니다.
    if title == '':
        for i in range(n):
            new = books[i][1]
            find(i, new, books[i][0])
        # 제목이 안 주어진 상태라면 모든 책을 순회하며 함수를 실행시켜줍니다.
    else:
        for i in range(num + 1, n):
            new = title + books[i][1]
            find(i, new, price + books[i][0])
        # 제목이 있다면 받은 인덱스 값 이후의 책을 이용하여 함수를 실행해줍니다.

find(0, '', 0)
print(result)
# 함수를 실행한 결과를 출력해줍니다.