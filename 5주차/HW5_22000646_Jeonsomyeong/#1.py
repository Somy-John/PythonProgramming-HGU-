fst = int(input("첫번째 정수를 입력하시오 : "))
snd = int(input("두번째 정수를 입력하시오 : "))

for i in range(0,snd):
    if i == 0:
        print(fst, end = ", ")
    else:
        result = fst + 2**i
        if i == snd-1:
            print(result)
        else:
            print(result, end = ", ")
