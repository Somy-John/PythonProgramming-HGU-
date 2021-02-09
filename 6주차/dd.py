from collections import Counter
import random

a = []
b = []

# Make list a by random.
for i in range (30):
    x = random.randint(1,30)
    a.append(x)


print(a)
count = 0

result = Counter(a)
print(result)

for key in result:
    for i in range(30):    
        if result[key]>=count:
            count = result[key]
    
for key in result:    
    if result[key]==count:
            b.append(key)
            b.append(result[key])

print(b)
print("가장 많이 반복된 수와 빈도수: ", end = '')

print(str(b[0])+",", str(b[1])+"회", end = '')

if len(b) >= 3:
    for i in range(2, len(b),2):
        print(", "+str(b[i])+",", str(b[i+1])+"회", end = '')
