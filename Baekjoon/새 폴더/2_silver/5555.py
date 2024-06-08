target = input()
result = 0
# 찾는 단어를 받고 단어가 몇개 찾을수있는지 담을 변수를 설정합니다.
for _ in range(int(input())):
    ring = input()
    ring += ring[:len(target)]
    # 반지의 문자를 받고 반지의 마지막 문자가 첫 문자와 이어 확인할수있도록 찾는 단어의 길이만큼 더해줍니다.
    if target in ring:
        result += 1
        # 찾는 단어가 있는지 확인해줍니다.
    
print(result)
# 찾는 단어가 몇 개의 반지에 있는지 출력해줍니다.