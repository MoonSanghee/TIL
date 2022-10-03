word = input()
stack = []
num = 0
cut = 0
for i in word:
    if i == '(':
        cut = 0
        stack.append(i)
    else:
        if cut == 1:
            num += 1
            stack.pop()
        else:
            stack.pop()
            num += len(stack)
            cut = 1
print(num)