n = int(input())
# 주어지는 문자의 개수를 받아줍니다
for _ in range(n):
    word = input()
    cnt = 0
    # 문자를 받고 와우의 개수를 담을 변수를 정해줍니다
    for i in range(len(word) - 2):
        if word[i: i + 3] == 'WOW':
            cnt += 1
            # 각 자리에서 와우가 이어지면 개수를 더해줍니다
    print(cnt)
    # 결과를 출력해줍니다