d = { 2: ('A', 'B', 'C'), 3: ('D', 'E', 'F'), 4:('G', 'H', 'I'), 5: ('J', 'K', 'L'), 6: ('M', 'N', 'O'), 7: ('P', 'Q', 'R', 'S'), 8: ('T', 'U', 'V'), 9: ('W', 'X', 'Y', 'Z') }
n = 1
while n == 1:
 i = input('10자리 문자열을 입력하시오 : ')
 if len(i) == 10:
   n = 2
 else:
    print("문자열이 10자리가 아닙니다. 다시 입력해주십시오")


rst = ''
r = 1
for j in i:
  if j.islower():
    j = j.upper()
  if r == 4 or r == 7 :
    rst += '-'
  for number , alpha in d.items():
    if j in alpha:
      rst += str(number)
  r += 1

print(rst)
