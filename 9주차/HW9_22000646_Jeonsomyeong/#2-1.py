def middle(s):
  if len(s) % 2:
    result = s[int(len(s)/2-0.5)]
  else:
    result = s[int(len(s)/2-1):int(len(s)/2+1)]
  return result

print(middle('middle'))
print(middle('midDle'))
