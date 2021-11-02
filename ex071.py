print('='*50)
print('Seja bem vindo ao caixa eletrônico 24 horas!')
print('='*50)
valor = int(input('Qual o valor que você gostaria de sacar? R$\n'))
total = valor 
céd = 50 
totcéd = 0
while True:
    if total >= céd:
        total -= céd 
        total += 1 
    else: 
        if totcéd > 0:
             print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0 
        if total == 0:
            break 
print('='*30)
print('Saque efetuado com sucesso!')
print('Volte sempre!')
print('='*30)

