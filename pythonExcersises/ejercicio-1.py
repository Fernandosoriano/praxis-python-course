################################################Ejercicio en clase:###################################################################
# nombre = input("Ingresa tu primer nombre y dos apellidos por favor:")
def incrementaSalario(nombre,edad,salario):
    arrNombre = nombre.split(' ')
    if(len(arrNombre) > 3):
        return print('sólo se aceptan nombres con un nombre y dos apellidos')
    # print(arrNombre[1][0])
    if(arrNombre[1][0].lower() == 'a'):
      salarioModificadoA = salario + 10
      print(f'hola {nombre} tu salario que era de: {salario} aumento 10 unidades y ahora es de: {salarioModificadoA}, pues tu apellido empieza con {arrNombre[1][0]}')
    else:
      salarioModificado = salario + 20
      print(f'hola {nombre} tu salario que era de: {salario} aumentó 20 unidades y ahora es de: {salarioModificado}, pues tu apellido empieza con {arrNombre[1][0]}')

# incrementaSalario(nombre,23,50)
####################################################TAREA SUDOKU#######################################################################################################
# """
# TAREA: generar un programa que rellene de manera aleatoria un numero en un sudoku
# 001|000|000
# 000|010|000
# 000|000|010
# -----------
# 000|001|000
# 000|000|001
# 010|000|000
# -----------
# 000|000|100
# 000|100|000
# 100|000|000
# """
numero = int(input('Por favor ingresa el número con el que deseas rellenar el sudoku '))

def formBoard (matrixSize):
        board = [ [ 0 for col in range(matrixSize**2) ] for row in range(matrixSize**2) ]
        # print(len(data))
        return board
# formBoard(3)
def rellenaBoard (board, numero):
  import random
  j = random.randint(0,8) #número de la columna colocada de manera aleatoria en alguna posición del primer renglón
  # print(f'el numero {numero} fue colocado en el primer renglón de manera aleatria en la columna: {j+1}')
  board[0][j] = numero  #rellenado de la columna elegida aleatoriamente del primer renglón, con el número que pasa el usuario 
  j2 = board[0].index(numero) # posición de la columna guardada en esta variable para poder usarlo como contador descendente en el else del siguiente for
  for i in range(len(board)):
      if any(elem != 0 for elem in board[i]): #checa si algun elemento del renglon uno es distinto de cero, para saltarnos esta parte de la iteración, y que no se coloque dos veces el número en el primer renglón
        continue
      if  j < len(board[0])-1:
        j = j + 1
        # print(i,j)
        board[i][j] = numero
      else:
        j2 = j2 - 1
        # print(i,j2)
        board[i][j2] = numero
  return (board)
# rellenaBoard(formBoard(3),3)

def printBoard(board):
  for i in range(len(board)):  #el índice i itera sobre el número de renglones
    if i % 3 == 0 and i  != 0:
      print('-------------')
    for j in range(len(board[0])): #el índice j itera sobre el número de columnas
      if j % 3 == 0 and j != 0:
        print("|", end = "")
      if j == 8:
          print(board[i][j])
      else:
       print(board[i][j], end="")
       
printBoard(rellenaBoard(formBoard(3),numero))
