n = int(input())
# 주어지는 닉네임의 개수를 받아줍니다
for _ in range(n):
    words = list(input().split())
    # 음절단위로 쪼개진것을 리스트형태로 받아줍니다
    words[0] = 'god'
    # 첫 음절을 god으로 바꿔줍니다
    result = ''.join(words)
    print(result)
    # 음절을 합친 결과를 출력해줍니다