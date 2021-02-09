def countVowels(s2):
  vowels = ['a','e','i','o','u']
  r = 0
  for i in vowels:
    r += s2.lower().count(i)
  result = '모음의 총 개수: %d'%r
  return result

print(countVowels('she sElls seashells by thE seashore'))
print(countVowels('Let`s learn python TOGETHER!'))
