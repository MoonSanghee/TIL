import sys

sys.stdin = open("1940_input.txt", "r")

t = int(input())
for i in range(1, t + 1):
    a = int(input())

    distance = 0
    speed = 0    

    for j in  range(a):
        command = list(map(str, input().split()))
        if command[0] == '1':
            speed += int(command[1])
            distance += speed
        elif command[0] == '2':
            speed -= int(command[1])
            if speed < 0:
                speed = 0
            distance += speed
        else:
            distance += speed

    print(f'#{i} {distance}')