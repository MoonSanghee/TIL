n = int(input())
# 문장의 수를 받아줍니다
for _ in range(n):
    words = list(input().split())
    new = words[2:] + words[:2]
    # 문장을 입력받고 처음 두 단어를 마지막으로 보낸 형태로 리스트를 만들어줍니다.
    print(*new)
    # 새로 만든 리스트를 출력해줍니다.