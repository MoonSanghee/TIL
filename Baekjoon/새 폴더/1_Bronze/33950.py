n = int(input())
# 단어의 개수를 받아줍니다
for _ in range(n):
    word = input()
    new = word.replace("PO", "PHO")
    print(new)
    # 주어지는 단어를 받아 수정한 결과를 출력해줍니다