f = open("poem.txt",'r')
#f2fw = open('numofWord.txt','a')
l = f.readlines()
for i in range(len(l)):
  temp = l[i].strip()
  templist = temp.split()
  n = len(templist)
  with open ('numofWord.txt','a') as f2fw:
      f2fw.write("%d\n"%n)
f.close()

f2fr = open('numofWord.txt','r')
print(f2fr.read())
f2fr.close()
