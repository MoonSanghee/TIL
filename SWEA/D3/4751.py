for i in range(int(input())):
    word = list(input())
    a = ['.']
    b = ['.']
    c = ['#']
    d = ['.']
    e = ['.']
    for i in range(len(word)):
        a.append('.#..')
        b.append('#.#.')
        c.append(f'.{word[i]}.#')
        d.append('#.#.')
        e.append('.#..')
    print(''.join(a))
    print(''.join(b))
    print(''.join(c))
    print(''.join(d))
    print(''.join(e))