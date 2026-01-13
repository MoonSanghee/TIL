n = int(input())
how = int(input())
# 주어지는 문의 수와 첫번째 문을 여는 방법을 받아줍니다
if n > 5:
    print('Love is open door')
    # 두 번째 규칙에 의해 홀수와 짝수 문의 여는 방법은 같을수 없는데 6이상일경우 3번문과 6번 문이 같을수 없으므로 규칙을 지킬수 없습니다
else:
    for i in range(1, n):
        if i % 2:
            print((how + 1) % 2)
        else:
            print(how)
    # 규칙을 지킬수있다면 결과를 출력해줍니다