import sys
def prime(num):
  if num <= 1 :
    print("처리할 수 없습니다.")
    sys.exit()
  d = []
  for i in range(2,num):
    if num % i == 0:
      d.append(i)
  if len(d) == 0:
    print("소수입니다")
  else:
    d.insert(0,1)
    d.append(num)
    print(d)

prime(2)
prime(6)
prime(-1)
