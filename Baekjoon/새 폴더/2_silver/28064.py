def check(x, y):
    length = min(len(x), len(y))
    for k in range(1, length + 1):
        if x[:k] == y[-k:] or x[-k:] == y[:k]:
            return True
    return False
# 이름이 연결되는지 확인하기 위한 함수를 만들어줍니다
n = int(input())
names = [input() for _ in range(n)]
# 이름의 개수와 이름들을 받아줍니다
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        cnt += check(names[i], names[j])
# 주어지는 모든 이름을 짝지어 연결되는지 확인하고 cnt에 연결되는 이름 쌍을 더해줍니다
print(cnt)
# 결과를 출력해줍니다