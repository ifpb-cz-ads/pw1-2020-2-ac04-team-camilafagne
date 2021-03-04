dividendo= int(input("Informe o primeiro número: "))
divisor= int(input("Informe o segundo número: "))

resto = dividendo
while resto >= divisor:
  resto = resto - divisor

print("O resto da divisão de %d por %d é %d" %(dividendo, divisor, resto))