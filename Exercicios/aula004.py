#  A   
#cont = 3
#while cont <= 12:
#    print(cont)
#    cont += 1
    
#for i in range (3,13):
#    print(i)

#  B
#cont2 = 0
#while cont2 < 9:   
#    print(cont2)
#    cont2 +=2

#for i2 in range (0,9,2):
#    print(i2)


#n1 = float(input('Digite um numero '))
#n2 = float(input('Digite outro numero '))
#
#operacao = input('---Escolha a operação desejada---\nSoma(+)\nMultiplicação(*)\nSubtração(-)\nDivisão(/)\nSair(s)\n')
#while operacao != 's':
#    if operacao == '+':
#        conta = n1 + n2
#        print('Resultado = {}'.format(conta))
#    elif operacao == '-':
#        conta = n1 - n2
#        print('Resultado = {}'.format(conta))
#    elif operacao == '*':
#        conta = n1 * n2
#        print('Resultado = {}'.format(conta))
#    elif operacao == '/':
#        conta = n1 / n2
#        print('Resultado = {}'.format(conta))
#    else:
#        print('Digite uma operação valida')
#    
#    n1 = float(input('Digite um numero '))
#    n2 = float(input('Digite outro numero '))
#    operacao = input('---Escolha a operação desejada---\nSoma(+)\nMultiplicação(*)\nSubtração(-)\nDivisão(/)\nSair(s)\n')
#print('Encerrando o programa')

while True:   
    n1 = int(input('Digite um numero '))
    n2 = int(input('Digite outro numero '))
    operacao = input('---Escolha a operação desejada---\nSoma(+)\nMultiplicação(*)\nSubtração(-)\nDivisão(/)\nSair(s)\n')
    
    if operacao == '+':
        conta = n1 + n2
        print('Resultado = {}'.format(conta))
        continue
    elif operacao == '-':
        conta = n1 - n2
        print('Resultado = {}'.format(conta))
        continue
    elif operacao == '*':
        conta = n1 * n2
        print('Resultado = {}'.format(conta))
        continue
    elif operacao == '/':
        conta = n1 / n2
        print('Resultado = {}'.format(conta))
        continue
    elif operacao == 's':
       break
    else:
        print('Digite uma operação valida')    
print('Encerrando o programa')


valor = int(input('Digite o valor em R$ '))

while True:
    if (valor >= 100):
        cedula100 = valor // 100
        valor -= cedula100*100
        print('Cédulas de 100: {}'.format(cedula100))
        if not valor:
            break
    if (valor >= 50):
        cedula50 = valor // 50
        valor -= cedula50*50
        print('Cédulas de 50: {}'.format(cedula50))
        if not valor:
            break
    if (valor >= 20):
        cedula20 = valor // 20
        valor -= cedula20*20
        print('Cédulas de 20: {}'.format(cedula20))
        if not valor:
            break
    if (valor >= 10):
        cedula10 = valor // 10
        valor -= cedula10*10
        print('Cédulas de 10: {}'.format(cedula10))
        if not valor:
            break
    if (valor >= 5):
        cedula5 = valor // 5
        valor -= cedula5*5
        print('Cédulas de 5: {}'.format(cedula5))
        if not valor:
            break
    if valor:
        cedula1 = valor
        print('Cédulas de 1: {}'.format(cedula1))
        break
