print('{:=^40}'.format('RVG Group'))
preço = float(input('Qual foi o valor da sua compra?R$:\n'))
print('''Qual vai ser a sua opção de pagamento?
[ 1 ] à vista dinheiro/cheque 
[ 2 ] à vista no cartão de débito 
[ 3 ] Parcelado no cartão de crédito em até 2x
[ 4 ] Parcelado no cartão de crédito em 3x ou mais ''') 
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = preço  - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela)) 
elif opção == 4:
    total = preço + (preço * 20 / 100)
    ttparcela = int(input('Quantas parcelas?'))
    parcela = total / ttparcela
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(ttparcela, parcela))
print('Sua compra foi no valor de {}R$ e o valor final com a opção de pagamento saiu por {}R$'.format(preço, total))
