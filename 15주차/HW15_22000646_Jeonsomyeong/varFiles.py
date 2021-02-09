f = open("sample.txt",'r')
f2 = open('result_sample1.txt','a')
name = f.readlines()
nn = 1
for i in name:
  n = len(i)
  if nn < 10:
    temp = i[3:n+1]
  else:
    temp = i[4:n+1]
  A = 0
  a = 0
  for j in temp:
    if j.isupper():
      A += 1
    elif j.islower():
      a += 1
  an = A + a
  tempstr = "%s %d, %d, %d\n"%(i[:n-1],A,a,an)
  f2.write(tempstr)
  nn += 1 
f2.close()
f3 = open('result_sample1.txt','r')
print(f3.read())

arp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rst = []
for k in arp:
  nnn = 1
  num = 0
  for l in name:
    if nnn < 10:
      if l[3] == k:
        num += 1
    else:
      if l[4] == k:
        num += 1
    nnn += 1
  if num > 0:
    rst += zip(k,str(num))
rstd = dict(rst)
print(rstd)
