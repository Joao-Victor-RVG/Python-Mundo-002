peso = float(input('Qual é o seu peso? (KG)\n'))
altura = float(input('Qual é a sua altura? (METROS)\n'))
imc =  peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está a baixo do peso normal')
elif 18.5 <= imc < 25:
    print('Parabéns, você está na faixa de peso normal!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO, CUIDADO!!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!, CUIDADO!')
elif 40<= imc:
    print('Você está com OBESIDADE MÓRBIDA, procure um médico o mais rápido possível')
print('Se você se encontra em algum quadro que não seja na faixa de peso NORMAl consulte um médico')




