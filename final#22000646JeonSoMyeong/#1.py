import random
import sys

def game():
  a = random.randrange(1,6,1)
  b = random.randrange(1,6,1)
  c = random.randrange(1,6,1)

  d = (a+b)*c

  print("a = %d"%a)
  print("c = %d"%c)
  print("(a+b)*c = %d"%d)

  r = 4
  while 1:
    i = input("b의 값은 무엇일까요? : ")
    if i == '%d'%b:
      print("정답입니다!!")
      sys.exit()
    elif i != b: 
      print("아쉽습니다... 남은 기회는 %d회"%(r-1))
      x = input("다시 하시겠습니까? (다시 하시려면 '네'라고 입력하세요) : ")
      if x == '네':
        pass
      else:
        sys.exit()
      r -= 1
    if r == 0:
      print("모든 기회가 끝이 났습니다...")

game()
