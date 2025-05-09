keyword = input()
# 주어지는 입력을 받아줍니다
UC = 0
DP = 0
# U와C, D와 P가 각각 헛깔릴수 있으므로 같이 세어줍니다
result = ''
for i in keyword:
    if i in 'CU':
        UC += 1
    else:
        DP += 1
# 각 문자의 수를 확인하여 담아줍니다
if UC > (DP + 1) // 2:
    result += 'U'
if DP > 0:
    result += 'DP'
# UC가 과반을 넘을수 있다면 U를 더하고 DP가 존재한다면 모든 UC를 C라고 할 때 D나 P는 최대가 될 수 있으므로 결과에 더해줍니다
print(result)
# 결과를 출력해줍니다