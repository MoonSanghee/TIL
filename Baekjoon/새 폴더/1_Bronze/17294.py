numbers = list(input())
# 주어지는 수를 받아줍니다
if len(numbers) == 1:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
    # 수가 한 자리라면 조건을 충족합니다
else:
    want = int(numbers[0]) - int(numbers[1])
    # 한자리 이상이라면 첫 두 수의 증가를 구하고
    for i in range(len(numbers) - 1):
        if int(numbers[i]) - int(numbers[i + 1]) != want:
            print('흥칫뿡!! <(￣ ﹌ ￣)>')
            break
        # 수를 순회하며 등차수열이 아닌지 확인해줍니다
    else:
        print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
        # 등차수열인지 확인해 주어진 조건대로 출력해줍니다.