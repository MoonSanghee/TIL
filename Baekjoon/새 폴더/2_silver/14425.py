n, m = map(int, input().split())
# 리스트에 들어가있는 단어의 수와 확인할 단어의 수를 받아줍니다.

s = set()
for _ in range(n):
    s.add(input())
# 단어를 넣어줄 s를 세트 형태로 만들고 n개의 단어를 받아 넣어줍니다.

cnt = 0
for _ in range(m):
    word = input()
    if word in s:
        cnt += 1
# m개의 단어를 받으면서 s안에 있다면 cnt의 값을 1씩 늘려줍니다.
print(cnt)
# cnt에 저장된 값을 출력해줍니다.