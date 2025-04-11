u, n = map(int, input().split())
# # 금액의 상한과 낙찰건수를 받아줍니다
d = dict()
for _ in range(n):
    s, p = input().split()
    p = int(p)
    if p in d:
        d[p].append(s)
    else:
        d[p] = [s]
# 딕셔너리를 만들어 낙찰 금액별로 낙찰받은 이름들을 리스트로 값을 가지게 넣어줍니다
arr = [(i, d[i]) for i in d]
arr.sort(key=lambda x : (len(x[1]), x[0]))
# 딕셔너리의 가장 적은 사람이 낙찰받은 수와 금액을 오름차순으로 정렬해줍니다
print(arr[0][1][0], arr[0][0])
# 주어진 조건에 맞게 낙찰받은 사람의 이름과 금액을 출력해줍니다