numero = int(input("Informe um numero: "))

if numero < 2: 
    print("O numero %d não é primo" % numero)
    
elif numero == 2: 
    print("O numero %d  é primo" % numero)

elif numero % 2 == 0: 
    print("O numero %d não é primo" % numero)

else: 
    for x in range(3, numero, 2):
        if numero % x == 0: 
            print("O numero %d não é primo" % numero)
            break
    else:
        print("O numero %d  é primo" % numero)
