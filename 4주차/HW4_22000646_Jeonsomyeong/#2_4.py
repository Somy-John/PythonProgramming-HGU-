fst = int(input("첫번째 정수를 입력하시오 : "))
snd = int(input("두번째 정수를 입력하시오 : "))

c = 0
d = 0
if fst > snd:
    if snd%2 == 0 :
         for i in range(snd+1,fst,2):
            c += 1
            d += i
    else:
        for i in range(snd+2,fst,2):
            c += 1
            d += i

else:
    if fst%2 == 0 :
         for i in range(fst+1,snd,2):
            c += 1 
            d += i
    else:
        for i in range(fst+2,snd,2):
            c += 1
            d += i

D = int(d/c)

print(D)
