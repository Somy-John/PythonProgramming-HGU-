import random
list1 = []
list2 = []
n = random.randint(1,7)
nn = random.randint(1,7)

if len(list1)>7 or len(list2)>7:
  exit()

for i in range(n):
  list1.append(random.randint(-5,5))
for h in range(nn):
  list2.append(random.randint(-5,5))

print('Test list 1 =',list1)
print('Test list 2 =',list2)

duplist = []
for j in list1:
  for jj in list2:
    if j == jj and duplist.count(j) == 0:
      duplist.append(j)
      

mm = 0
if len(duplist) == 0:
  print('no duplicate elements')
else:
  print('양 쪽 모두 존재하는 값 : ',end = '')
  for k in duplist:
    if mm == len(duplist)-1 :
       print(k)
    else:
      print(k,end=', ')
    mm+=1


  index1 = []
  index2 = []
  st = -1
  for l in duplist:
      for ll in range(list1.count(l)):
        index1.append(list1.index(l,st+1))
        st = list1.index(l)
      for lll in range(list2.count(l)):
        index2.append(list2.index(l,st+1))
        st = list2.index(l)

  index1.sort()
  index2.sort()
  print('Index 값 :',index1,',',index2)

for m in duplist:
  for mm in range(list1.count(m)):
    list1.remove(m)
  for mmm in range(list2.count(m)):
    list2.remove(m)

print("List1 :",list1)
print("List2 :",list2)
