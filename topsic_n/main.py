#上に凸

N = int(input())
y = list(map(int,input().split()))
y.insert(0,0)

#print(N,y)

#(i,y[i])と(i+2,a[i+2])を通る直線の式を求める（数学）y = a*x+b　（j = i + 2 とした）
#(i+1,y[i+1])とy座標を比較するため、式に間のx座標(k) を代入
#kを代入して求められたy座標と与えられたy[i+1]の代償を比較
#すべてのiのにおいて条件を満たせばOK

flag = True


for i in range(1,N-1):
    for j in range(i+2,N+1):
        for k in range(i+1,j):
            a = (y[j] - y[i])/(j - i)
            b = y[i] - a * i
            
            h = a * k + b
            #print(f"i = {i}, j = {j}, k = {k}")
            #print(f"y[k] = {y[k]}, h = {h}")

            if h < y[k]:
                continue
            else:
                flag = False
                break

if flag == True:
    print("YES")
else:
    print("NO")




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#flag = True
#count = 0

#for i in range(0,N-2):
#    if (A[i] < A[i+1] and A[i+1] < A[i+2]) or (A[i] > A[i+1] and A[i+1] > A[i+2]):
#        #print(f"A[i] = {A[i]}, A[i+1] = {A[i+1]}, A[i+2] = {A[i+2]}")
#        continue
#    else:
#        count += 1
#    
#    if count > 1:
#        flag = False
#        break
#
#if flag == True:
#    print("YES")
#else:
#    print("NO")