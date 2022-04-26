#モンスターの名前

S = input()
N = int(input())
list_S = list(S)

for i in range(0,N):
    list_S.insert(0,"a")
    #print(list_S)

print("".join(list_S))
