"""
def fact(n):
  fact_lst = []
  if n == 1:
    fact_lst.append(1)
  f = n * fact(n-1)
  fact_lst.append(f)
  return fact_lst

print(fact(5))
print(fact(20))
"""
# 위의 코드(11주차 1번문제)는 어딘가 에러가 있어서 그 때문에 뒤의 코드(2번)이 작동되지 않았습니다. 그래서 주석처리 하였습니다!
# 어떤 부분에서 오류가 있는지 알고싶습니다! 감사합니다.

import random
import sys

def select(listname,n):
  if n <1:
    print("error")
    sys.exit()
  result = []
  for i in range(n):
    tempN = random.randrange(0,len(listname))
    x = listname.pop(tempN)
    result.append(x)
  print(result)


select([1,2,3,4,5,6,7], 2)
select(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'], 3)
select([2,4,6,8,10,12], 0)
