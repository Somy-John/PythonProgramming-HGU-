n1 = int(input("숫자 1: "))
n2 = int(input("숫자 2: "))
n3 = int(input("숫자 3: "))
n4 = int(input("숫자 4: "))
n5 = int(input("숫자 5: "))
n6 = int(input("숫자 6: "))
n7 = int(input("숫자 7: "))

#1. 가장 큰 숫자를 고른다.
L = n1
if n2 > L:
    L = n2
if n3 > L:
    L = n3
if n4 > L:
    L = n4
if n5 > L:
    L = n5
if n6 > L:
    L = n6
if n7> L:
    L = n7

#2. 가장 작은 숫자를 고른다.
s = n1
if n2 < s:
    s = n2
if n3 < s:
    s = n3
if n4 < s:
    s = n4
if n5 < s:
    s = n5
if n6 < s:
    s = n6
if n7 < s:
    s = n7
    
#3. 두번째로 큰 숫자를 고른다. (가장 큰 숫자보다 작으면서 가장 작은 수보다 큰 숫자가 계속 s가 돼서 골라내는 원리.)
if n1 < L and n1>s:
    s = n1
if n2 < L and n2>s:
    s = n2
if n3 < L and n3>s:
    s = n3
if n4 < L and n4>s:
    s = n4
if n5 < L and n5>s:
    s = n5
if n6 < L and n6>s:
    s = n6
if n7 < L and n7>s:
    s = n7


if n1==n2 and n2==n3 and n3==n4 and n4==n5 and n5==n6 and n6==n7:
    print("동일한 수")
else:
    print("두번째로 큰 수는",str(s)+"입니다.")
