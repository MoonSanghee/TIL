n, s = input().split()
result = 0
# 확인할 아이템의 수와 포함될 단어를 받고 삭제된 총 수량을 담을 변수를 설정해줍니다
for _ in range(int(n)):
    name, brick = input().split()
    name = list(name.split('_'))
    # 아이템의 이름과 개수를 받고 아이템을 이루어진 다어를 구별하여 리스트에 감아줍니다
    if s in name:
        result += int(brick)
    # 확인할 단어가 있는지 확인해줍니다
print(result)
# 삭제된 아이템의 개수를 출력해줍니다