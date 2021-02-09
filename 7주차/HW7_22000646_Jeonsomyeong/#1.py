list1 = []
for i in range(1,11):
  l = int(input("%d번째 수를 입력하시오 : "%i))
  list1.append(l)

print("리스트 :",list1)
a = list1.pop(9)
list1.insert(0,a)
print("오른쪽으로 한 칸씩 이동 :", list1)
b = list1.pop(4) + list1.pop(4)
print("중간에 위치한 2개의 element 제거 :",list1)
L = list1[0]
for lc in list1:
  if lc > L:
      L = lc

print("전체 element 중 가장 큰 수 : %d"%L)
SUM = sum(list1)
N = SUM/8

jn = 0
kn = 0
d_list = []

for j in list1:
  if list1.count(j) > 1 and j != '*':
    da = [list1.index(j),list1.index(j,list1.index(j)+1)]
    d_list.append(da)
    for jjj in range(list1.count(j)):
      rj = list1.index(j)
      list1.remove(j)
      list1.insert(rj,'*')

if bool(d_list):
  print("중복여부 체크 : exist duplicate elements")
  print("중복되는 index :",end = '')
  for k in range(len(d_list)):
    print(d_list[k], end = '')
  print('')
  if N - int(N) == 0 :
    print("저장된 값들의 합계, 평균 : %d, %d"%(SUM,N))
  else:
    print("저장된 값들의 합계, 평균 : %d, %.1f"%(SUM,N)) 

else:
  print("중복여부 체크 : no duplicate elements")
  if N - int(N) == 0 :
    print("저장된 값들의 합계, 평균 : %d, %d"%(SUM,N))
  else:
    print("저장된 값들의 합계, 평균 : %d, %.1f"%(SUM,N))
