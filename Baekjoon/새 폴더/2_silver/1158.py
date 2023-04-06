n, k = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
# n명의 사람과 몇번째마다 뺄건지를 받아줍니다
num = 0
# 빠질 위치의 사람을 표시해줄 변수를 정해줍니다.
out = []
# 빠진사람을 차례로 저장해줄 리스트를 정해줍니다.
for i in range(n):
    num += k - 1
    if num >= len(numbers):
        num = num%len(numbers)
    # k간격만큼 확인하며 남은 사람보다 길어졌다면 남은 사람으로 나눈 몫으로
    # 값을 갱신해줍니다
    out.append(str(numbers.pop(num)))
    # out에 numbers의 num인덱스 자리에 위치한 사람을 꺼내서 문자열 형으로 넣어줍니다.
print('<', ', '.join(out),'>', sep='')
# 주어진 조건에 맞추어 출력해줍니다