a = ' abcdefghijklmnopqrstuvwxyz'
A = a.upper()
def crypt(str):
  result = ''
  for i in str:
    if i.isupper():
      if A.find(i)%2 == 1:
        result += A[A.find(i)+1]
      if A.find(i)%2 == 0:
        result += A[A.find(i)-1]
    elif i == ' ':
      result += ' '
    else:
      if a.find(i)%2 == 1:
        result += a[a.find(i)+1]
      if a.find(i)%2 == 0:
        result += a[a.find(i)-1]
  print(result)

def decrypt(str):
  result = ''
  for i in str:
    if i.isupper():
      if A.find(i)%2 == 1:
        result += A[A.find(i)+1]
      if A.find(i)%2 == 0:
        result += A[A.find(i)-1]
    elif i == ' ':
      result += ' '
    else:
      if a.find(i)%2 == 1:
        result += a[a.find(i)+1]
      if a.find(i)%2 == 0:
        result += a[a.find(i)-1]
  print(result)
  
crypt("Abc")
decrypt("Bad")
crypt('Zoo Park')
decrypt('Ypp Obql')
