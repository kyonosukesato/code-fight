N = int(input())

sum = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        if i % j == 0:
            sum = sum + j
    
print(sum)
