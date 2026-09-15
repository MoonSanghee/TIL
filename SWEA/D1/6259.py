alpha = 0
digits = 0

code = input()

for i in code:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digits += 1

print(f'LETTERS {alpha}')
print(f'DIGITS {digits}')