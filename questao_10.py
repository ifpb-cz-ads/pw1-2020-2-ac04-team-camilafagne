deposito = float(input("Informe o valor do depósito: "))
taxa_juros = float(input("Informe a taxa de juros de uma poupança em porcentagem: ")) 

valor = deposito
total = 0


for x in range(12):
  valor =  valor + (deposito * taxa_juros/100)
  print("Mês %d: R$%.2f" % (x+1, valor))
  total= total + valor

print("Valor total do ganho de juros: R$%.2f" % total)