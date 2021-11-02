from random import randint
from time import sleep
v = 0
while True:
    jogador = int(input('Digite um valor:\n'))
    computador = randint (0, 10)
    total =  jogador + computador 
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]\n')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    print('Deu Par!' if total % 2 == 0 else 'Deu Ímpar!')
    if tipo == 'p':
        if total % 2 == 0:
            print('Você Ganhou!')
            v += 1 
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Ganhou!')
            v += 1 
        else:
            print('Você PERDEU!')
            break 
    print('Vamos Jogar novamente....')
sleep(2)
print(f'Game Over! Você venceu {v} vezes.')








