import random
mlist = []
m = 0
list1 = []
#밑의 두 list1은 문제에 적혀있던 test list1과 test list2 입니다.
#list1 = [10, 10, 11, 11, 1, 10, 5, 7, 19, 7, 3, 11, 7, 15, 16, 20, 9, 7, 4, 2, 3, 11, 20, 14, 5, 15, 2, 14, 20, 6]
#list1 = [14, 9, 2, 20, 15, 2, 5, 14, 7, 8, 19, 9, 3, 14, 6, 11, 8, 16, 14, 2, 5, 20, 14, 15, 12, 18, 20, 7, 14, 5]
print("Test list1")
for i in range (30):
    x = random.randint(1,30)
    list1.append(x)
print(list1)

for j in range(30):
    n = list1.count(list1[j])
    if n > m:
        m = n
        mlist.clear()
        mlist.append(list1[j])
        
    if n == m:
        if mlist.count(list1[j])==0:
            mlist.append(list1[j])
    #print(n, m, mlist)

#print(mlist)

h = len(mlist)
mlist.reverse()
    
print("가장 많이 반복된 수와 빈도 수 :", end=' ')
    
for g in range(h):
    if g != h-1:
        print(str(mlist[g])+', '+"%d회"%m ,end=', ')
    else:
        print(str(mlist[g])+', '+"%d회"%m)
