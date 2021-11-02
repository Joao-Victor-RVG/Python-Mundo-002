soma = cont =  0 
while True:
    num = int(input('Digite um número\n'))
    if num == 999:
        break
    cont += 1 
    soma += num
print(f'A soma dos valores digitados anteriormente {cont} é de {soma} !!')