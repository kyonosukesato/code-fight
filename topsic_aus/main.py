#ジャングルジム

N = int(input())
A = list(map(int, input().split()))
B = []

for h in reversed(A):
    B.append(h)

rf = 0
lf = 0

for i in range(N-1):
    rf += max(0,A[i+1] - A[i])
    lf += max(0,B[i+1] - B[i])

    #print(f"rf = {rf}, lf = {lf}")

print(min(rf,lf))