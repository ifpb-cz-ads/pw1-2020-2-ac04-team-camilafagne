quantidade = int(input("Informe a quantidade: "))
codigo = int(input("Informe o código: "))

total_compras = 0

while(codigo >= 1):

  if codigo == 1:
    total_compras = total_compras + (0.50 * quantidade)

  elif codigo == 2:
    total_compras = total_compras + (1.00 * quantidade)

  elif codigo == 3:
    total_compras = total_compras + (4.00 * quantidade)

  elif codigo == 5:
    total_compras = total_compras + (7.00 * quantidade)
  
  elif codigo == 9:
    total_compras = total_compras + (8.00 * quantidade)

  else:
    print("Ação inválida")

  quantidade = int(input("\nInforme a quantidade: "))
  codigo = int(input("Informe o código: "))

print(f"Total Compras: R${total_compras:.2f}")



