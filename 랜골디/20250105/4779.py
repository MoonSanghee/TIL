result = []
answer = '-'
for _ in range(13):
    result.append(answer)
    answer = answer + ' ' * len(answer) + answer
# 정답으로 출력되는 12까지의 경우를 만들어 리스트에 담아줍니다
while True:
    try:
        n = int(input())
        print(result[n])
    except:
        break
    # 주어지는 수를 확인하여 원하는 결과를 출력해줍니다