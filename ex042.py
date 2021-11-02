r1 = float(input('Primeiro segmento:\n'))
r2 = float(input('Segundo segmento\n'))
r3 = float(input('terceiro segmento\n'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um  triângulo ' , end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else: 
        print('ISÓSCELES')
else:
    print('Não pode formar um triângulo com essa combinação de retas')