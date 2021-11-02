num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar:]\n'))
    soma += num 
    cont +=  1 
print('Você digitou {} números e a soma ente eles foi {}'.format(cont, soma))


