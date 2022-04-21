N = int(input())
a = list(map(int, input().split()))

#print(N,a)

a_s  = sorted(a)
#print(a_s)

ans = a_s[1]
print(ans)