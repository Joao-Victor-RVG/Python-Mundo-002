resp = 's'
soma = quantidade = media = maior = menor = 0 
while resp in 'Ss':
    num = int(input('Digite um número:\n'))
    soma += num 
    quantidade += 1 
    if quantidade ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num 
        if num < menor:
            menor = num 
    resp = str(input('Quer continuar?? [S/N]\n')).upper().strip() [0]
media = soma / quantidade
print('Você digitou {} números e a média foi {}'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))






