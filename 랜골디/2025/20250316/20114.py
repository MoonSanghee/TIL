n, h, w = map(int, input().split())
now = [input() for _ in range(h)]
# 문자의 원래 길이와 번진 영역의 크기를 받아줍니다
result = ['?'] * n
# 원래 문자의 크기와 같은 결과를 담을 리스트를 만들어줍니다
for i in range(n):
    for j in range(h):
        for k in range(w):
            letter = now[j][k + i * w]
            if letter != '?':
                result[i] = letter
# 원래 문자의 자리부터 번진 영역을 확인하여 원래 문자를 확인할 수 있으면 갱신해줍니다
print(''.join(result))
# 확인한 원래 문자를 출력해줍니다