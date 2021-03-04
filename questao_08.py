num_1= int(input("Informe o primeiro número: "))
num_2= int(input("Informe o segundo número: "))


resultado = num_1
cont= 0
while resultado >= num_2:
  resultado = resultado - num_2
  cont = cont + 1

print("A divisão de %d por %d é %d e o resto é %d" %(num_1, num_2, cont, resultado))
