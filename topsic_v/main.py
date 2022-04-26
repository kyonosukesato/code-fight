N = int(input())
S = input()
#print(N,S)

count = 1

for i in range(1,N):
    if S[i-1] == S[i]:
        continue
    else:
        count += 1

print(count)