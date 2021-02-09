Y = int(input("출생년도를 입력하시오:"))
M = int(input("태어난 달을 입력하시오:"))

if M<=3:
    O = 2020-Y+1
else:
    O = 2020-Y

print(O,"세")
