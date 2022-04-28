#ジャングルジム

from audioop import reverse


N = int(input())
A = list(map(int, input().split()))

rf = 0
lf = 0

for i in range(N-1):
    rf += max(0,A[i+1] - A[i])
#print(rf)

for j in range(N,1,-1):
    lf = max(0, A[i-1] - A[i])
#print(lf)

print(max(rf,lf))