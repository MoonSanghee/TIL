n = int(input())
# 문장의 개수를 받아줍니다.
for i in range(n):
    words = list(input().split())
    # 문장을 받아줍니다.
    new = ' '.join(words[::-1])
    # 단어를 거꾸로 조합한 문장을 만들어줍니다.
    print(f'Case #{i + 1}: {new}')
    # 몇번째 어떤 문장이 오는지 출력해줍니다.