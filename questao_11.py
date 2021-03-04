
taxa_juros = float(input("Informe a taxa de juros de uma poupança em porcentagem: ")) 

anterior = 0
total = 0
valor = 0

for x in range(12):
  deposito = float(input("Informe o valor do depósito do mes %d: " % (x+1)))
  valor = deposito
  valor =  valor + anterior + (deposito * taxa_juros/100)
  anterior = valor

  print("Mês %d: R$%.2f" % (x+1, valor))
  total= total + valor

print("Valor total do ganho de juros: R$%.2f" % total)