def facto(num):
  f = [1]
  for i in range(2,num+1):
    temp = 1
    for ii in range(2,i+1):
      temp *= ii
    f.append(temp)
  print(f)

facto(10)
facto(17)
