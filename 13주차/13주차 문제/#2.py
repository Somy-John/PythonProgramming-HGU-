a = 'abcdefghijklmnopqrstuvwxyz'
h = 'mnovwxpqrstuabcghideflyzjk'
def code():
  cd = {}
  for i in range(len(a)):
    cd[a[i]] = h[i]
    cd[a[i].upper()] = h[i].upper()
  return cd

def decode():
  dcd = {}
  for i in range(len(a)):
    dcd[h[i]] = a[i]
    dcd[h[i].upper()] = a[i].upper()
  return dcd

cd = code()
dcd = decode()
l = []; ll = []
s = input("문자열을 입력하시오 : ")
for i in range(len(s)):
  k = cd.get(s[i])
  l.append(k)
coded = ''.join(l)

for i in range(len(coded)):
  k = dcd.get(coded[i])
  ll.append(k)
decoded = ''.join(ll)
print('입력 문자열이 "%s"를 암호화 하면 "%s", "%s"를 복호화 하면 "%s"이다.'%(s,coded,coded,decoded))

if s == decoded:
  print('"%s"는 입력된 값"%s"와 동일하다!!'%(decoded,s))
else:
  print('"%s"는 입력된 값"%s"와 동일하지 않다!!'%(decoded,s))
