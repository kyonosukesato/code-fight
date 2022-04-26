H, W, Q = map(int, input().split())
q = [input().split() for _ in range(Q)]

mat = [["."] * W for _ in range(H)]

#print(q)
#print(H,W,Q)
#print(mat)

for i in range(0,Q):
    mat[int(q[i][0])-1][int(q[i][1])-1] = q[i][2]
#print(mat)

for j in range(0,H):
    print("".join(mat[j]))