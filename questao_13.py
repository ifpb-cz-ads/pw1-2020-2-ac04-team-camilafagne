
n = -1
cont = 0
soma = 0
while n:
  n = int(input("Informe um número qualquer (para parar digite 0): "))
  if n == 0:
    break
  cont = cont + 1
  soma = soma + n
  
media = soma / cont

print("Você digitou %d numeros, a soma de todos os numeros digitados foi %d e a média desses numero foi de %d" % (cont, soma, media))
