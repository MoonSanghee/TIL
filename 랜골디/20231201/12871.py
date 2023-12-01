s = input()
t = input()
ns = s
nt = t
while len(ns) != len(nt):
    if len(ns) > len(nt):
        nt += t
    elif len(nt) > len(ns):
        ns += s
if ns == nt:
    print(1)
else:
    print(0)