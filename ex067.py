while True:
    n = int(input('Quer ver a tabuada de qual valor??\n'))
    print('-='*30)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c} ')
    print('-='*30)
print('Muito obrigado por usar o nosso programa!')
print('Te ajudar é sempre um prazer! Volte sempre s2s2')



