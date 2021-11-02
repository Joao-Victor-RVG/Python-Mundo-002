nota01 = float(input('Qual foi sua primeira nota?\n'))
nota02 = float(input('Qual foi sua segunda nota?\n'))
media = (nota01 + nota02) / 2
print('Sua primeira nota foi {:.1f} e a sua segunda nota foi {:.1f} ,então a sua média ficou igual a {:.1f}'.format(nota01, nota02, media))
if 7 > media >=5:
    print('O aluno está de em RECUPERAÇÃO')
elif media <5:
    print('O aluno está REPROVADO!')
elif media >=7:
    print('O aluno foi APROVADO, Parabéns!!!')
