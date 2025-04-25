n = int(input())
arr = list(map(int, input().split()))
others = sorted(arr[1:])
# 플레이어수와 각 플레이어의 공격력을 받아줍니다
# 준원이를 제외한 나머지 플레이어들을 오름차순으로 정렬하여줍니다
for i in others:
    if i < arr[0]:
        arr[0] += i
    else:
        print("No")
        break
# 준원이가 나머지 플레이어들을 차례대로 모두 죽일 수 있다면 Yes 아니면 No를 출력해줍니다
else:
    print("Yes")