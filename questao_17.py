n = int(input("Informe um numero: "))

y = 1
cont2 = 0
while cont2 < n:
  x=y
  cont=0
  while x >= 1:
    if y % x == 0:
      cont = cont + 1
    x = x-1
  if cont == 2:
    print("%d"%(y))
    cont2 = cont2 + 1
  y = y + 1
  