def CountFile(filename):
  try:
    with open(filename,'r') as f:
      l = f.readlines()
  except IOError:
    print('파일을 찾을 수 없습니다.')
    import sys
    sys.exit()

  ll = []
  for i in range(len(l)):    # 줄바꿈 제외
    ll.append(l[i].replace('\n',''))

  for ii in range(ll.count('')):  # '' 제외
    ll.remove('')

  sum1 = 0 #공백 포함
  sum2 = 0 #공백 제외
  sum3 = 0 #단어 수
  sum4 = 0 #줄 수

  lll = []
  for i in ll:
    t = ''
    for ii in i:
      if ii != ' ':
        t += ii
    lll.append(t)

  for jj in range(len(lll)):
    sum1 += len(lll[jj])

  for iii in range(len(ll)):
    sum2 += len(ll[iii])

  for jjj in range(len(ll)):
    templist = ll[jjj].split(' ')
    sum3 += len(templist)
  for k in range(len(ll)):
    if ll[k] != '':
      sum4 += 1
  print("단어 수:", sum3)
  print("문자 수(공백 제외):", sum1)
  print("문자 수(공백 포함):", sum2)
  print("줄 수:", sum4)
  return sum1, sum2, sum3, sum4

CountFile("hi.txt")
