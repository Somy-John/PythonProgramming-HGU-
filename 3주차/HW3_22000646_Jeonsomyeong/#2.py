h = float(input("키 입력: "))
w = float(input("몸무게 입력: "))

h = h/100

BMI = w/(h*h)
B = str(BMI)

if BMI < 18.5:
    result = "저체중 입니다."
elif BMI >= 18.5 and BMI < 25.0:
    result = "정상 입니다."
elif BMI >= 25.0 and BMI <30.0:
    result = "과체중 입니다."
else:
    result = "비만 입니다."

print("BMI 수치는",B[:4],"이며,",result)
