a = input("Input str : ")
l = []
for i in range(len(a)):
  b = tuple([i,a[i]])
  l.append(b)
print(l)
