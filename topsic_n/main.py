#上に凸

N = int(input())
y = list(map(int,input().split()))
y.insert(0,0)

flag = True


for i in range(1,N-1):
    for j in range(i+2,N+1):
        for k in range(i+1,j):
            a = (y[j] - y[i])/(j - i)
            b = y[i] - a * i
            
            h = a * k + b

            if h < y[k]:
                continue
            else:
                flag = False
                break

if flag == True:
    print("YES")
else:
    print("NO")