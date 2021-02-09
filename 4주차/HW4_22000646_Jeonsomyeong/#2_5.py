n = input("정수를 입력하시오 : ")

N = len(n)
l = []
i = 0
SUM = 0

while i < N:
    t = i
    s = int(n[t])
    l.append(s)
    i += 1

for i in l:
    SUM += i

print("결과는 %d입니다."%SUM)
