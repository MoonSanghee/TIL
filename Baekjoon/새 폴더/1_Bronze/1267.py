n = int(input())
used = list(map(int, input().split()))
# 몇 통의 전화를 했는지 각 통화의 시간을 담아줍니다.
m = 0
y = 0
# 두 요금제의 비용을 저장할 값을 설정해줍니다.

for i in used:
    y += 10 * (i // 30) + 10
    m += 15 * (i // 60) + 15
    # 각 요금제는 30, 60초로 나눈 몫에 요금을 곱한 후 1번의 요금을 더 더한 값입니다.

if m < y:
    print(f'M {m}')
    # m의 요금제가 더 싸면 M과 얼마의 요금이 나왔는지
elif y < m:
    print(f'Y {y}')
    # y의 요금제가 더 싸면 Y와 얼마의 요금이 나왔는지
else:
    print(f'Y M {y}')
    # 같으면 Y M 과 얼마의 요금이 나왔는지 출력해줍니다.