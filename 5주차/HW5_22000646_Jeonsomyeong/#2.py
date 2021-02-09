I = int(input("출력할 단 수를 입력하시오 : "))

if I > 15 or I < 2:
    print("2~ 15 값 중 정수를 입력하세요. 17은 처리할 수 없습니다!")
else:
    for i in range(2,I+1):
        for j in range(1,10):
            c = i * j
            print("%d * %d = %d"%(i,j,c))
