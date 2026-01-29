maps = [list(input().split()) for _ in range(15)]
# 사진을 받아줍니다
for line in maps:
    if 'w' in line:
        print('chunbae')
        break
    elif 'b' in line:
        print('nabi')
        break
    elif 'g' in line:
        print('yeongcheol')
        break
    # 고양이는 한 마리만 존재하므로 고양이 영역이 존재하는지 확인하여 어떤 고양이의 사진인지 출력해줍니다