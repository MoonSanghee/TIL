n = int(input())
key = input()
# 입력이 주어지는 단어의 수와 나열된 단어를 받아줍니다.
bigdata = list(key.split("bigdata"))
security = list(key.split("security"))
# bigdata와 security를 기준으로 입력 단어를 나누어 각각 리스트에 담아줍니다.
if len(bigdata) > len(security):
    print("bigdata?")
elif len(bigdata) < len(security):
    print("security!")
else:
    print("bigdata? security!")
# 리스트의 길이를 비교하여 주어진 형식에 맞게 출력해줍니다.