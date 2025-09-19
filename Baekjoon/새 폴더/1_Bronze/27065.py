t = int(input())

types = [0] * 5001
answers = []
# 5000이하의 모든 수의 상태를 담을 변수와 찾는 조건에 맞는 수를 담아둘 리스트를 만들어줍니다

for i in range(1, 5001):
    number = 0
    flag = True
    # 약수의 합을 담을 변수와 모든 약수가 과잉수가 아닌지 확인할 변수를 설정해줍니다
    for j in range(1, i):
        if i % j == 0:
            number += j
            if types[j] == 2:
                flag = False
            # 약수가 과잉수라면 찾는 조건에서 걸러줍니다
    if number == i:
        types[i] = 1
    elif number > i:
        types[i] = 2
        if flag:
            answers.append(i)
    # 약수의 합을 확인하여 부족수가 아니라면 값을 갱신하고 찾는 조건에 부합하다면 리스트에 담아줍니다
    
for _ in range(t):
    n = int(input())
    if n in answers:
        print("Good Bye")
    else:
        print("BOJ 2022")
    # 테스트 케이스를 받고 결과를 출력해줍니다