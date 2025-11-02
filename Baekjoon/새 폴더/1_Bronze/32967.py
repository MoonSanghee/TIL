words = ["bigdata", "public", "society"]
flag = False
# 공공 빅데이터의 단어들을 받고 주제가 공공빅데이터인지 확인할 변수를 설정해줍니다
title = input()
for word in words:
    if word in title:
        flag = True
# 주제를 받고 공공 빅데이터의 필수 단어가 포함되는지 확인해줍니다
if flag:
    print("public bigdata")
else:
    print("digital humanities")
# 결과를 출력해줍니다