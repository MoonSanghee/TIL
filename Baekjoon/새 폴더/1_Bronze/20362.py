n, s = input().split()
n = int(n)
answer = ''
chat = []
# 주어지는 채팅의 수와 정답자의 닉네임을 받고 정답과 채팅을 담을 변수를 만들어줍니다
for _ in range(n):
    nickname, comment = input().split()
    if answer == '':
        if nickname != s:
            chat.append(comment)
        else:
            answer = comment
    # n개의 닉네임과 입력을 받고 정답이 나오지 않았다면 정답이 나올때까지 입력을 리스트에 담고 
    # 정답이 입력되었다면 이후의 입력을 리스트에 추가하지 않습니다

result = chat.count(answer)
print(result)
# chat에서 정답의 수를 확인하여 출력해줍니다