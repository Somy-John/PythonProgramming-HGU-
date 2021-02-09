def mergeSort(list1, list2):
  list1.sort()
  list2.sort()
  result = []
  n1 = 1
  n2 = 1
  while n1 > 0 or n2 > 0: # 둘 다 result로 옮겨질 때 까지 반복
    n1 = len(list1)
    n2 = len(list2)
    if n1 > 0 and n2 > 0: # 리스트1과 2 대소비교, 둘 중 하나가 result로 다 옮겨질 때 까지
      if list1[0] > list2[0]:
        result.append(list2[0])
        list2.pop(0)
      elif list2[0] > list1[0]:
        result.append(list1[0])
        list1.pop(0)
      else:
        result.append(list1[0])
        list1.pop(0)
        list2.pop(0)
    elif n1 > 0:           # 리스트2가 먼저 다 옮겨졌을 때
      result.append(list1[0])
      list1.pop(0)
    elif n2>0:             # 리스트1이 먼저 다 옮겨졌을 때
      result.append(list2[0])
      list2.pop(0)
  print(result)

c = [2, 4, 5, 7, 7, 9, 15]
d = [3, 7, 9, 9, 9, 16]
e = [-3, 0, 1, 3, 3, 5, 10, 10]
f = [-7, -7, 0, 3, 7, 9]

mergeSort(e,f)
