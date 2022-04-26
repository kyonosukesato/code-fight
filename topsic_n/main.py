#上に凸

N = int(input())
A = list(map(int,input().split()))
#print(N,A)

flag = True
count = 0

for i in range(0,N-2):
    if (A[i] < A[i+1] and A[i+1] < A[i+2]) or (A[i] > A[i+1] and A[i+1] > A[i+2]):
        #print(f"A[i] = {A[i]}, A[i+1] = {A[i+1]}, A[i+2] = {A[i+2]}")
        continue
    else:
        count += 1
    
    if count > 1:
        flag = False
        break

if flag == True:
    print("YES")
else:
    print("NO")