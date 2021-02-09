s = input("화학식을 입력하시오 : ")
temp = 0
d = []
n = 1
for i in s:
  try:
    g = int(s)
    d.append(temp*g)
    n = 1
  except ValueError:
    if n == 2:
      d.append(temp)
    if i == 'O':
      temp = 15.9994
    if i == 'S':
      temp = 32.066
    if i == 'C':
      temp = 12.011
    if i == 'H':
      temp = 1.00794
    if i == 'N':
      temp = 14.00674
    n = 2
S = sum(d)

print(s,"분자량은",S)
