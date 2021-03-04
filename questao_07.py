n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))

cont = 0
resultado = 0

while cont < n2:
  resultado = resultado + n1
  cont = cont + 1

print("O resultado da multiplicação de %d x %d é %d" %(n1, n2, resultado))