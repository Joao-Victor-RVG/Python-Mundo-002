total = totmil =  cont = barato = 0 
while True:
    produto = str(input('Nome do produto:\n'))
    preço = float(input('Preço: R$\n'))
    cont += 1 
    total += preço
    if preço > 1000:
        totmil += 1 
    if cont ==1:
        menor = preço 
        barato = produto
    else:
        if preço < menor:
            menor = preço 
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(' {:-^40}'.format('FIM do programa!'))
print(f'O total da compra foi R${total:.2f}')
print(f'A quantidade de produtos vendidos a cima de mil reais foi {totmil} produtos')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')




