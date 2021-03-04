menu = -1
while menu != 0:
  menu = int(input("Digite 1 para realizar uma adição \nDigite 2 para realizar uma subtração \nDigite 3 para realizar uma multiplicação \nDigite 4 para realizar uma divisão \nDigite 0 para sair: "))
  
  if menu == 1:
    n = int(input("Informe o numero que deseja ver a tabuada: "))
    x = 0
    while x <= 10:
      resultado = n + x 
      print("%d + %d = %d \n" % (x, n, resultado))
      x = x + 1

  if menu == 2:
    n = int(input("Informe o numero que deseja ver a tabuada: "))
    x = n
    for y in range(0 , 10, 1):
      resultado = x - n
      print("%d - %d = %d \n" % (x, n, resultado))
      x = x + 1
      
  if menu == 3:
    n = int(input("Informe o numero que deseja ver a tabuada: "))
    x = 0
    while x <= 10:
      resultado = n * x 
      print("%d x %d = %d \n" % (x, n, resultado))
      x = x + 1

  if menu == 4:
    n = int(input("Informe o numero que deseja ver a tabuada: "))
    x = 0
    for y in range(1 , 11, 1):
      x = x + n
      resultado = x / n 
      print("%d / %d = %d \n" % (x, n, resultado))
      
      
print("Até a proxima! ^-^")