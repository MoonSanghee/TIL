n = int(input())
# 입력받을 문장의 수를 받아줍니다.
for i in range(n):
    word = input()
    # 문장을 받아줍니다.
    print(str(i + 1) + '. ' + word)
    # 문장의 순서를 문자열로 바꾸어 '. '를 붙이고 문장과 함께 출력해줍니다.