n = int(input())

if n % 100 != 0:
    print("-1")
else:
    a = n // 500
    b = (n % 500)/100
    count = a + b
    print(count)