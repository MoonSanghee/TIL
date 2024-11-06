socks = []
for _ in range(5):
    n = int(input())
    if n in socks:
        socks.remove(n)
    else:
        socks.append(n)
# 양말을 차례대로 받아 짝이 맞으면 빼주어서 남는 양말을 확인해줍니다
print(socks[0])