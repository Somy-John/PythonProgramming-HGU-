def vowelchar(str):
  vowel = ['a','e','i','o','u','A','E','I','O','U']
  result = ''
  for i in str:
    if i in vowel:
      result += i
  print(result)

vowelchar('apple')
vowelchar('banana')

def sorted(a,b,c,d):
  if a >= b >= c >= d or a <= b <= c <= d:
    print('True')
  else:
    print('False')
    
sorted(2, 8, 12, 16)
sorted(3, 0, 3, 0)

def numDigit(n):
  ns = str(n)
  if '.' in ns:
    N = ns.split('.')
    ni = len(N[0])
    nf = len(N[1])
    print("정수 자리 수 %d, 소수 자리 수 %d"%(ni,nf))
  else:
    print("정수 자리 수 %d, 소수 자리 수 0"%len(ns))  

numDigit(3.12)
numDigit(119.0)
