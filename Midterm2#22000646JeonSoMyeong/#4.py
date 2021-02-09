word=[ 'apple', 'box', 'bus', 'cantus', 'dish', 'knife', 'lady', 'pitch', 'stimulus', 'wish', 'wolf' ]
plural = {}
for i in word:
  n = len(i)-1
  if i[-1] == 'y':
    temp = i[0:n] + 'ies'
    plural[i] = temp
  elif i[-1] == 'f':
    temp = i[0:n] + 'ves'
    plural[i] = temp
  elif i[n-1:n+1] == 'fe':
    temp = i[0:n-1] + 'ves'
    plural[i] = temp
  elif i[n-1:n+1] == 'us':
    temp = i[0:n-1] + 'i'
    plural[i] = temp
  elif i[-1] == 's' or i[-1] == 'x' or i[-1] == 'z':
    temp = i + 'es'
    plural[i] = temp
  elif i[n-1:n+1] == 'ch' or i[n-1:n+1] == 'sh':
    temp = i + 'es'
    plural[i] = temp
  else:
    temp = i + 's'
    plural[i] = temp
print(plural)
