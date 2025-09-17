name = input()
# 암호화된 이름을 받아줍니다
base = {
        "northlondo": "NLCS",
        "branksomeh": "BHA",
        "koreainter": "KIS",
        "stjohnsbur": "SJA"
    }
# 네 학교의 이름들의 앞에서부터 10개의 알파벳을 소문자로 매칭하여 딕셔너리에 담아줍니다
for n in range(26):
    find = ""
    for char in name:
        code = (ord(char) - ord('a') - n) % 26
        find += chr(ord('a') + code)
    # 한 칸씩 미루며 이름을 복호화해줍니다
    if find in base:
        print(base[find])
        break
    # 복호화한 이름의 매칭되는 값이 존재한다면 이름을 출력하고 반복을 멈추어줍니다