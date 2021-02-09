n = input("영문명사를 입력하세요 : ")
l = len(n)

def pluralize (N):
  if N[-1] == 'y':
    p = N[0:l-1] + 'ies'
  elif N[-1] == 'f':
    p = N[0:l-1] + 'ves'
  elif N[-1] == 's' or N[l-2:l] == 'ch' or N[l-2:l] == 'sh':
      p = N + 'es'
  else:
    p = N + 's'
  print(p)

pluralize(n)
