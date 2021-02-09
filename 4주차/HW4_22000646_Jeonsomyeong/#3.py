n = input("정수를 입력하시오 : ")
f = 1

try:
    if int(n)<= 0 or float(n)-int(n) != 0 :
        print("양의 정수가 아니기 때문에 계산 할 수 없습니다.")

    else:
        n = int(n)
        for j in range(n):
            f *= j+1
            J = j+1
            if j == n-1:
                print("%d! = %d"%(J,f) , end = "")
            else:
                print("%d! = %d"%(J,f) , end = ", ")

except ValueError as error:
    print("양의 정수가 아니기 때문에 계산 할 수 없습니다.")
