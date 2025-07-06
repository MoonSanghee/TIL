n, m = map(int, input().split())
# 주어지는 총 복무일수와 완료한 복무일수를 받아줍니다
total = int((m / n) * 60 * 24)
# 주어지는 진행도를 24시간과 60분을 곱해 진행도를 전체 분으로 몇 분이나 진행했는지 구해줍니다
hour = total // 60
minute = total % 60
# 시간과 분으로 바꾸어줍니다
print(f"{hour:02d}:{minute:02d}")
# 주어진 방식대로 출력해줍니다