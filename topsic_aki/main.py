#ほぼ昇順

N = int(input())
S = input()

a = list(S)
c = list(S)


ans = 0

for i in a:
    a = list(S)
    b = list(S)
    b.sort()

    #print(i)

    a.remove(i)
    b.remove(i)

    #print(f"a = {a}")
    #print(f"b = {b}")

    if a == b:
        ans = c.index(i) + 1
        break

if ans != 0:
    print(ans)
else:
    print("-1")
