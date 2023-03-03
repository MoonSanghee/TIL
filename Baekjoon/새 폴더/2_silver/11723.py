import sys

n = int(sys.stdin.readline())
status = set()
# 숫자를 add 된 수들을 담아줄 형태로 set을 만들어줍니다.

for i in range(n):
    word =  sys.stdin.readline().strip().split()
    if len(word) == 1:
        if word[0] == 'all':
            status = set([i for i in range(1, 21)])
        else:
            status = set()
    # 길이가 하나일경우 'all이라면 1부터 20까지 넣어주고
    # 아니라면 'empty'이므로 비워줍니다.
    else:
        command, num = word[0], word[1]
        num = int(num)
        # 길이가 둘이라면 명령어와 숫자를 받으므로 
        # num을 정수형으로 바꾸어줍니다.
        if command == 'add':
            status.add(num)
        elif command == 'remove':
            status.discard(num)
            # 명령어가 add라면 num을 넣어주고
            # remove라면 num을 제거해줍니다.
        elif command == 'check':
            if num in status:
                print(1)
            else:
                print(0)
                # 명령어가 check라면 status안에 있는지 확인하고 있다면 1 없다면
                # 0을 출력해줍니다.
        elif command == 'toggle':
            if num in status:
                status.discard(num)
            else:
                status.add(num)
                # toggle이라면 있다면 없애주고 없다면 추가해줍니다.