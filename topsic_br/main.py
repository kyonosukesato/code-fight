#数列の操作

#
# 並び変える回数は訊かれていないので考えない。
# 等しい要素があれば消す。
# 残った要素を昇順に並べ替え、対応する要素の差の絶対値の合計を求める
# 

import abc


N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_l = sorted(a)
b_l = sorted(b)

count = 0

for i in a:
    for j in b:
        if i == j:
            a_l.remove(i)
            b_l.remove(j)

for k in range(len(a_l)):
    count += abs(a_l[k] - b_l[k])
print(count)