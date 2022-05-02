# 決議
import math
from math import ceil

N, G, A = map(int, input().split())

a = N // 2
b = a + 1

#Maxを計算する

i = A // b
MAX = min(G,i)

#minを計算する

j = A // a
not_majo = min(G,j) * a
k = (A - not_majo) / b
MIN = math.ceil(k)

print(MAX,MIN)
