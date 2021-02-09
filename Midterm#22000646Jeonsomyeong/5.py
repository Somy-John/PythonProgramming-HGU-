sam1=[1, 53, 19, 5, 21, -12, -3, 32, 11, 25]
sam2=[1, 5, 10, 12, -3, 23, 19, 20, 55]
for i in sam1:
  if i in sam2:
    sam2.remove(i)
sam = sam1 + sam2

def bubble_S(listname):
  l = len(listname)
  for i in range(l):
    for j in range(0, l-i-1):
        if listname[j] > listname[j+1]: 
            listname[j], listname[j+1] = listname[j+1], listname[j]
  print(sam)

bubble_S(sam)
