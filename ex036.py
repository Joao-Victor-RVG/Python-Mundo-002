vcasa = float(input('Qual é o valor da casa que você gostaria de financiar?\n'))
vsalario = float(input('Qual é o seu salário fixo que você ganha por mês??\n'))
anos = int(input('Em quantos anos você gostaria de pagar pela casa?\n'))
prestação =  vcasa / (anos * 12)
minimo = vsalario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(vcasa, anos))
print('A prestação será de R${:.2f}'.format(prestação)), 
if prestação <= minimo:
    print('Parabêns o seu empréstimo foi aprovado pelo banco, consulte um de nossos gerentes')
else:
    print('O empréstimo NÃO foi concetido pelo banco, para mais informações consulte o nosso SAC pelo número 0800-708-6969 ')


