n = int(input())
result = 0
# 챕터수와 필요한 시간들을 받아줍니다
while n:
    left = 30
    while left > 0 and n:
        t = int(input())
        n -= 1
        if left >= t or left / t >= (1 / 2):
            result += 1
        left -= t
    # 챕터를 완료하면 표시를 하고 30분까지 남은 시간까지 챕터의 절반 이상을 완료할 수 있다면 표시해줍니다
print(result)
# 절반 이상 완료한 챕터의 수를 출력해줍니다