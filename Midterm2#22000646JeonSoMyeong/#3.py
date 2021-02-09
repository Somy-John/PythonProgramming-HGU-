def fibo(n):
  if n == 1:
    return [1]
  elif n == 2:
    return [1,1]
  else:
    list = fibo(n-1)
    f = list[n-3] + list[n-2]
    list.append(f)
    return list
print(fibo(10))
