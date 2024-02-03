pitch = int(input())
report = list(map(int, input().split()))
base = [0, 0, 0, 0]
ballcount = 0
for ball in report:
    if ball == 1:
        ballcount += 1
        if ballcount == 4:
            for i in range(1, 4):
                if base[i]:
                    base[i] = 0
                    base[i - 1] += 1
            base[3] = 1
            ballcount = 0
    elif ball == 2:
        ballcount = 0
        for i in range(1, 4):
                if base[i]:
                    base[i] = 0
                    base[i - 1] += 1
        base[3] = 1
    else:
         ballcount += 1
         for i in range(1, 4):
                if base[i]:
                    base[i] = 0
                    base[i - 1] += 1
         if ballcount == 4:
              ballcount = 0
              base[3] = 1
print(base[0])