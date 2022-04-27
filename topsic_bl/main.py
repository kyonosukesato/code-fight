#タイピングの秒数計算

S = input()
list_C = ["a","s","d","f","g","h","j","k","l"]

T = S

for i in range(9):
    T = T.replace(list_C[i],str(i + 1))
#print(T)

int_list = list(map(int, T))
int_list.insert(0,1)
#print(int_list)

sum = 0
#print(len(S))

for j in range(len(S)):

    sum = sum + abs(int_list[j] - int_list[j+1]) + 1
print(sum)
