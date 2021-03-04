lista = [1,7,2,4]
menor = lista[0]
for elemento in lista:
	if elemento < menor:
    		menor = elemento
print("O menor número da lista é: %d" % menor)
