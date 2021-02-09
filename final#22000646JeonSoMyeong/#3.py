# 소수 확인하기 - 수정

def isprime(num):
  prime=True
  if num == 1:
    prime=False
  else:
    for i in range(2,num):
      if num%i==0:
        prime=False
        break
  return prime

print(isprime(1))
print(isprime(2))
print(isprime(4))

# def what( s1, s2):  - 수정
# s1, s2는 문자열 s2는 한 글자 문자열로  #지정하여, s1에 s2가 존재하면 그 위치를 #모두 리스트로 만들어서 출력

def what(s1,s2):
  n=[]
  for i in range (len(s1)):
    if s1[i]==s2:
      n.append(i)
  print(n)

what('jeonsomyeong','o')

# def fact(n):

# 재귀함수로 코딩, 1!, 2!, 3!, ……..n! 값을

# 리스트로 만들어서 return 한다

def fact(n):
  if n ==1:
    rst = []
    factn = 1
    rst.append(factn)
  else :
    factn = n*fact(n-1)[0]
    rst.append(factn)

  return rst
print(fact(5))


# 암호화, 복호화 문제
d = {'A' : 'M', 'a' : 'm', 'B' : 'N', 'b' :'n', 'C' : 'O', 'c' : 'o', 'D' : 'V', 'd' : 'v', 'E' :'W', 'e' : 'w', 'F' : 'X', 'f' : 'x', 'G' : 'P','g' : 'p', 'H' : 'Q', 'h' : 'q', 'I' : 'R', 'i' : 'r', 'J' : 'S', 'j' : 's', 'K' : 'T', 'k' : 't', 'L' : 'U', 'l' : 'u', 'M' : 'A', 'm' : 'a', 'N' : 'B', 'n' : 'b', 'O' : 'C', 'o' : 'c', 'P' : 'G', 'p' : 'g', 'Q' : 'H', 'q' : 'h', 'R' : 'I', 'r' : 'i','S' : 'D', 's' : 'd', 'T' : 'E','t' : 'e', 'U' : 'F', 'u' : 'f', 'V' : 'L', 'v' : 'l', 'W' : 'Y', 'w' : 'y', 'X' : 'Z', 'x' : 'z', 'Y' : 'J', 'y' : 'j', 'Z' : 'K', 'z' : 'k'}
d2 =     diction = {'M' : 'A', 'm' : 'a', 'N' : 'B', 'n' : 'b', 'O' : 'C', 'o' : 'c', 'V' : 'D', 'v' : 'd', 'W' : 'E', 'w' : 'e', 'X' : 'F', 'x' : 'f', 'P' : 'G', 'p' : 'g','Q' : 'H', 'q' : 'h', 'R' : 'I', 'r' : 'i', 'S' : 'J', 's' : 'j', 'T' : 'K', 't' : 'k', 'U' : 'L', 'u' : 'l', 'A' : 'M', 'a' : 'm', 'B' : 'N', 'b' : 'n', 'C' : 'O', 'c' : 'o', 'G' : 'P', 'g' : 'p', 'H' : 'Q', 'h' : 'q', 'I' : 'R', 'i' : 'r', 'D' : 'S', 'd' : 's', 'E' : 'T', 'e' : 't', 'F' : 'U', 'f' : 'u', 'L' : 'V', 'l' : 'v', 'Y' : 'W', 'y' : 'w', 'Z' : 'X','z' : 'x', 'J' : 'Y', 'j' : 'y', 'K' : 'Z', 'k' : 'z'}
def code(dic,word):
  code=""
  for alpha in word:
    if alpha in dic.keys():
      code=code+dic[alpha]

  return code

word=input("문자열을 입력하세요:")

word2=code(d,word)

if word == code(d2,word2):
  print (word,"는",code(d2,word2),"와 동일하다!!")

else:

    print ("암호화가 제대로 되지 않음.")
