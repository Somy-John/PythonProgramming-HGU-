#숫자야구
import random
c_list = random.sample(range(0, 10), 4)
# 중복 확인 함수
def check_list(listname,input_num):
  if listname.count(input_num) == 0:
    R = 'T'
  else:
    R = 'F'
  return R

# 숫자야구 실행
stk = 0
Try = 0
while stk < 4:
  p_list = []
  for i in range(4):
    n = int(input("Input a number : "))
    while n < 0 or 9 < n : # 0~9 사이의 값 나올 때까지 반복
      print("Please input a number from 0 to 9")
      n = int(input("Input a number : "))
    while check_list(p_list, n) == 'F': # 중복되지 않는 값 넣을 때까지 반복
      print("please input another num")
      n = int(input("Input a number : "))
    p_list.append(n)

  # strike or ball 판정
  stk = 0
  ball = 0
  for j in range(4):
    if c_list[j] == p_list[j]:
      stk += 1
    elif c_list[j] in p_list:
      ball += 1
  print("%d-strike, %d-ball"%(stk,ball))
  print()
  Try += 1
print()
if Try == 1:
  print("You win! 1st try..")
elif Try == 2:
  print("You win! 2nd try..")
elif Try == 3:
  print("You win! 3rd try..")
else:
  print("You win! %dth try.."%Try)
