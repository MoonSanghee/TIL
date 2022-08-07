test_case =int(input())

for test_num in range(1, test_case + 1):
    bush = input()

    cnt = 0

    for i in range(len(bush) - 1):
        if bush[i] == '(' and bush[i + 1] == '|':
            cnt += 1
        
        if bush[i + 1] == ')' and bush[i] == '|':
            cnt += 1

    print(f'#{test_num} {bush.count("()") + cnt}')