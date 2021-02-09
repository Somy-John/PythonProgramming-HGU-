f=['apple', 'avocado', 'BANANA', 'blueberry', 'coconut', 'lemon', 'LIME', 'mango', 'papaya', 'PEACH', 'strawberry']
N = 0
l = []
for i in f:
  vowels = ['a','e','i','o','u','A','E','I','O','U']
  if i[1] in vowels:
    l.append(i)
for ii in l:
  f.remove(ii)
print(f)
