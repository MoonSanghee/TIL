book = dict()
N = int(input())

for i in range(N):
    name = input()
    if name not in book:
        # 책이 키 값에 값이 없으면 밸류 1로 설정
        book[name] = 1
    else:
        book[name] += 1
        # 있으면 1씩 더해준다

count = 0
result = []

for i in book:
    if book[i] > count:
        count = book[i]
        result = [0]
        result[0] = i
    # 카운트 갯수가 갱신되면 리스트를 i값만을 가지도록 갱신해준다.
    elif book[i] == count:
        result.append(i)
    # 동수가 있을시 result라는 리스트에 추가해준다.

result = sorted(result)
# 알파벳 순으로 정리해준다.
print(result[0])
# 결과값을 출력한다.