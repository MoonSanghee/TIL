import sys
input = sys.stdin.readline

k, l = map(int, input().split())
# 두 수를 받아줍니다.
wait = dict()

for i in range(l):
    num = input().strip()
    wait[num] = i
    # 각 수를 받아 새로 나왔다면 수서를 뒤에 나온 차례로 갱신해줍니다.
result = sorted(wait.items(), key = lambda x:x[1])
# 차례순으로 정렬하여줍니다.
if (k > len(result)):
    k = len(result)
# 원하던 길이가  충분히 길지 않다면 현재 딕셔너리의 길이만큼 출력한다고 갱신해줍니다.
for i in range(k):
    print(result[i][0])
# 출력해야하는 길이만큼만 출력해줍니다.