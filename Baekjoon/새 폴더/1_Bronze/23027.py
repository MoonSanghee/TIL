S = input()
# 주어지는 문장을 받아줍니다
if "A" in S:
    S = S.replace("B", "A")
    S = S.replace("C", "A")
    S = S.replace("D", "A")
    S = S.replace("F", "A")
elif "B" in S:
    S = S.replace("C", "B")
    S = S.replace("D", "B")
    S = S.replace("F", "B")
elif "C" in S:
    S = S.replace("D", "C")
    S = S.replace("F", "C")
else:
    S = len(S) * "A"
# 주어지는 문장을 주어진 조건을 차례대로 확인하며 A, B, C가 있다면 바꿔야하는 문자들만 바꾸고 셋 다 없다면 전부 A로 바꾸어줍니다
print(S)
# 결과를 출력해줍니다