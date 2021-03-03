valor_divida = float(input("Informe o valor inicial da dívida: "))

taxa_juros = float(input("Informe a taxa de juros de uma poupança em porcentagem: ")) 

valor_mensal = float(input("Informe o valor que será pago mensalmente: "))
  
mes = 0
total_valor = 0
total_juros = 0

if(valor_divida == taxa_juros or valor_mensal <= taxa_juros):
  print("Impossível pagar a conta!")

else:
  while valor_divida > 0:
    mes = mes + 1
    juros = valor_divida * (taxa_juros /100)
    valor_divida = valor_divida + juros - valor_mensal
    total_valor += valor_divida
    total_juros = total_juros + juros
    print("%.2f" % valor_divida)

  print(f"O valor total pago: R${total_valor:.2f}")

  print("O número de meses para pagar a dívida é %d mes(es)" % mes)

  print(f"O total de juros que foi pago: R${total_juros:.2f}")
