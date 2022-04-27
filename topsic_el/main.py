#品切れ

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
#print(N,A,B)

for i in range(N):
    if A[i] < B[i]:
        print(i + 1)