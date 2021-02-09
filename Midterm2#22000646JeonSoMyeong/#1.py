def Ispal(string1):
  s = string1.replace(" ","")
  ss = s.replace(",","")
  sss = ss. replace("!","")
  c = []
  for i in range(len(sss)):
    if sss[i].isupper():
      c.append(sss[i].lower())
    else:
      c.append(sss[i])
  n = int(len(c)/2) + 1
  tn = 0
  for j in range(n):
    if c[j] == c[-(j+1)]:
      tn = tn + 1
  if tn == n:
    return True
  else:
    return False
print(Ispal("Rise to vote!!!!, sir"))
