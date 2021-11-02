from datetime import date 
print('''Qual é o seu sexo?
[ 1 ] FEMININO
[ 2 ] MASCULINO''')
opçao = int(input('Qual opção você se intentifica? 1 OU 2 \n'))
if opçao == 1:
    print('O alistamento nas forças armadas não é obrigatoria para pessoas do sexo FEMININO')
else:
    print('O alistamento é obrigatorio para pessoas do sexo MASCULINO')
atual = date.today().year
nasc = int(input('Ano de nascimento:\n'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc , idade, atual))
if idade == 18:
    print('Você tem que se alistar esse ano')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para poder se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já passou da idade de fazer o alistamento, deveria ter ocorrido há  {} anos atrás'.format(saldo))
    ano = atual - saldo
    print('O seu alistamento foi em {}'.format(ano))



