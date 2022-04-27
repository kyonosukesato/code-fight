#右折

N = int(input())
d = [int(input()) for _ in range(N)]
#print(N,D)

x = 0
y = 0

for i in range(N):
    if i % 4 == 0:
        x += d[i]
    elif i % 4 == 1:
        y -= d[i]
    elif i % 4 == 2:
        x -= d[i]
    else:
        y += d[i]
    
#print(f"(x,y) = ({x},{y})")
print(x,y)
