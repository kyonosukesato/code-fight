# 互いに異なる

n = int(input())
a = list(map(int,input().split()))
#print(n,a)

flag = True

for i in range(n):
    for j in range(n):
        #print(f"i = {i}, j = {j}, a[i] = {a[i]}, a[j] = {a[j]}")

        if i != j and a[i] == a[j]:
            flag = False
            break

if flag == True:
    print("YES")
else:
    print("NO")
