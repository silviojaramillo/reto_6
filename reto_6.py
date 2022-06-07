import random

#Definiendo los elementos y el número para cada uno
elements = ['Piedra', 'Papel', 'Tijera']
winners = []

#Elemento de la computadora
intentos = 0
while intentos < 5:
    print('Ingrese un número según sea el elemento que desea usar')
    print('Ingrese 0 si su elemento deseado es PIEDRA')
    print('Ingrese 1 si su elemento deseado es PAPEL')
    print('Ingrese 2 si su elemento deseado es TIJERA')
    player = int(input('Ingrese su elección: '))
    elementPlayer = elements[player]
    list_computer = random.sample(elements,1)
    elementComputer = list_computer[0]
    if (elementPlayer == 'Piedra' and elementComputer == 'Papel'):
        print('Tú has seleccionado {} y computer ha seleccionado {}'.format(elementPlayer,elementComputer))
        print('El ganador de esta ronda es Computer')
        winners.append('Computer')
        intentos += 1
    elif (elementPlayer == 'Piedra' and elementComputer == 'Tijera'):
        print('Tú has seleccionado {} y computer ha seleccionado {}'.format(elementPlayer,elementComputer))
        print('El ganador de esta ronda es User')
        winners.append('User')
        intentos += 1
    elif(elementPlayer == 'Papel' and elementComputer == 'Tijera'):
        print('Tú has seleccionado {} y computer ha seleccionado {}'.format(elementPlayer,elementComputer))
        print('El ganador de esta ronda es Computer')
        winners.append('Computer')
        intentos += 1
    elif(elementPlayer == 'Papel' and elementComputer == 'Piedra'):
        print('Tú has seleccionado {} y computer ha seleccionado {}'.format(elementPlayer,elementComputer))
        print('El ganador de esta ronda es User')
        winners.append('User')
        intentos += 1
    elif(elementPlayer == 'Tijera' and elementComputer == 'Piedra'):
        print('Tú has seleccionado {} y computer ha seleccionado {}'.format(elementPlayer,elementComputer))
        print('El ganador de esta ronda es Computer')
        winners.append('Computer')
        intentos += 1
    elif(elementPlayer == 'Tijera' and elementComputer == 'Papel'):
        print('Tú has seleccionado {} y computer ha seleccionado {}'.format(elementPlayer,elementComputer))
        print('El ganador de esta ronda es User')
        winners.append('User')
        intentos += 1
    elif elementPlayer == elementComputer:
        print('Tú has seleccionado {} y computer ha seleccionado {}'.format(elementPlayer,elementComputer))
        print('Han elegido el mismo elemento, no hay ganador')
        intentos = intentos

user = winners.count('User')
system = winners.count('Computer')
if(user > system):
    print('El ganador de la partida es {} con {} puntos'.format('Usuario',user))
else:
    print('El ganador de la partida es {} con {} puntos'.format('Sistema',system))

