n, k = map(int, input().split())
public = list(map(int, input().split()))
private = list(map(int, input().split()))
# 주어지는 카드의 개수와 제거할 카드의 수를 받아줍니다
for _ in range(k):
    result = -1e9
    x = 0
    for i in public:
        for j in private:
            if i * j > result:
                result = i * j
                x = j
    private.remove(x)
    # 모든 경우를 확인해 최선의 카드를 제거해줍니다
answer = -1e9

for i in public:
    for j in private:
        answer = max(answer, i * j)
# 모든 조건을 순회하여 최대로 만들어지는 값을 찾아줍니다
print(answer)
# 결과를 출력해줍니다