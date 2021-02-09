def bubble(listname):
  L = len(listname)
  for i in range(L):
    for j in range(0, L-i-1):
      if listname[j] > listname[j+1]: 
        listname[j], listname[j+1] = listname[j+1], listname[j]
  return listname

def merge(list1,list2):
  l1 = bubble(list1)
  l2 = bubble(list2)
  d = 0
  result = []
  n1 = 1
  n2 = 1
  while n1 > 0 or n2 > 0:
    n1 = len(l1)
    n2 = len(l2)
    if n1 > 0 and n2 > 0:
      if l1[0] > l2[0]:
        result.append(l2[0])
        l2.pop(0)
      elif l2[0] > l1[0]:
        result.append(l1[0])
        l1.pop(0)
      else:
        result.append(l1[0])
        l1.pop(0)
        l2.pop(0)
        d = d + 1
    elif n1 > 0:
      result.append(l1[0])
      l1.pop(0)
    elif n2>0:
      result.append(l2[0])
      l2.pop(0)
  return result , d

import random
I = []
for i in range(31):
  I.append(i)
list1 = random.sample(I,10)
list2 = random.sample(I,10)
print(merge(list1,list2))
