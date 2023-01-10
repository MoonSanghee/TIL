n = int(input())
ch = [input() for _ in range(n)]
# 채널의 길이와 각 채널을 입력받습니다.
button = ''
first = ch.index('KBS1')
button += first * '1' + first * '4'
# 'KBS1'이 위치한 인덱스 위치를 찾아 1을 인덱스 자리만큼 4를 인덱스 자리만큼 차례대로 눌러줍니다.
second = ch.index('KBS2')
if first > second:
    button += (second + 1) * '1' + second * '4'
    # 'KBS1'이 더 뒤에 있었다면 'KBS2'가 한 칸 밀려났으므로 1을 인덱스보다 한 번 더 눌러주고
    # 이동은 인덱스 만큼만 시켜줍니다.
else:
    button += second * '1' + (second - 1) * '4'
    # 아니라면 인덱스만큼 화살표를 옮겨주고 이동은 1칸 덜 시켜줍니다.
print(button)
# 입력한 버튼을 출력해줍니다.