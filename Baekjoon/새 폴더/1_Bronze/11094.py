n = int(input())
# 주어지는 문장의 수를 받아줍니다
for _ in range(n):
    line = input()
    if line[:10] == 'Simon says':
        print(line[10:])
        # 주어지는 문장이 Simon says로 시작한다면 지시사항을 출력해줍니다