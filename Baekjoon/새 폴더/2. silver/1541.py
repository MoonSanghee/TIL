sen = list(map(str, input().split('-')))
for i in range(len(sen)):
    sen[i] = list(map(int, sen[i].split('+')))
if len(sen) == 1:
    result = sum(sen[0])
else:
    result = sum(sen[0])
    for i in range(1, len(sen)):
        result -= sum(sen[i])
print(result)
# split메서드를 이용하여 '+', '-' 같은 기호를 기준으로도 문자열을 나눌 수 있다.
# 이를 활용하여 -가 나오면 그 이후의 모든 값들을 빼주고 아니면 모든 값듫을 다 더하도록 구현하면된다.