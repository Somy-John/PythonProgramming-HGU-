L = []
n = 1

for i in range(10):
    i = int(input("%d번째 수를 입력하시오 : "%n))
    L.append(i)
    n += 1

print("정렬 전 :",L)

Len = len(L)

for i in range(Len):
    for j in range(0, Len-i-1):
        if L[j] > L[j+1]: 
            L[j], L[j+1] = L[j+1], L[j] 

print("정렬 후 :",L)
