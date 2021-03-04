n = int(input("Tabuada de: "))
inicio = int(input("Informe um número onde deseja que inicie a tabuada: "))
fim = int(input("Informe um número onde deseja que finalize a tabuada: "))

if inicio > fim:
  print("Ação inválida")
else:
  while inicio <= fim:
    resultado = n * inicio
    print("%d x %d = %d \n" % (inicio, n, resultado))
    inicio = inicio + 1
