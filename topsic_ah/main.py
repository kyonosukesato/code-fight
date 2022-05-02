#アスタリスクな道路

import math

N, M = map(int, input().split())
a =[list(map(int,input().split())) for _ in range(M)]

comb = 0

def combinations_count(n,r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

F6 = math.factorial(6)

for i in range(1,N+1):
    lis = []
    for j in range(M):
        if i in a[j]:
            lis.append(a[j])

    if len(lis) >= 6:
        comb += combinations_count(len(lis),6)

print(comb * F6)
