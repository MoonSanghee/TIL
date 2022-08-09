import sys
sys.stdin =open('1240_input.txt', 'r')

test_case = int(input())
numbers = {
    '1011000': 0,
    '1001100': 1,
    '1100100': 2,
    '1011110': 3,
    '1100010': 4,
    '1000110': 5,
    '1111010': 6,
    '1101110': 7,
    '1110110': 8,
    '1101000': 9
}
for test in range(1, test_case + 1):
    n, m = list(map(int, input().split()))

    output = 0
    for i in range(n):
        line = str(input())
        if int(line) != 0:
            line = str(int(line[::-1]))
            code = []
            for j in range(8):
                code.append(numbers[line[j*7:j*7+7]])
            check = code[0]
            for j in range(1, 8):
                if j % 2 == 1:
                    check += code[j]*3
                else:
                    check += code[j]
            if check % 10 == 0:
                output = sum(code)
            else:
                output = 0

    print(f'#{test} {output}')
    