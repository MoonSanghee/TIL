n = int(input())
d = dict()
# 파일의 수와 파일의 수를 담을 딕셔너리를 만들어 줍니다.
for _ in range(n):
    name, file = input().split('.')
    # .을 기준으로 확장자를 확인해줍니다.
    if file in d:
        d[file] += 1
    else:
        d[file] = 1
    # 딕셔너리에 담아줍니다.

result = sorted(d.items(), key = lambda x : x[0])
# 딕셔너리의 값을 사전순으로 정렬하여줍니다.
for key, value in result:
    print(key, value)
    # 확장자와 나온 횟수를 출력해줍니다.