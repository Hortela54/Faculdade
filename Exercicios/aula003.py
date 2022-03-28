lado1 = float(input('Digite a primeira medida do triangulo'))
lado2 = float(input('Digite a segunda medida do triangulo'))
lado3 = float(input('Digite a terceira medida do triangulo'))


if lado1 == 0 or lado2 == 0 or lado3 == 0:
    print("O valor não pode ser menor ou igual a 0")
else:
    if lado1 > lado2+lado3 or lado2 > lado1+lado3 or lado3 > lado1+lado2:
        print('Um lado não pode ser maior que a soma dos outros dois lados')
    else:    
        if lado1 == lado2 and lado2 == lado3:
            print('O triangulo é Equilatero')
        elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:  
            print('O triangulo é Isósceles')
        else:
            print('O o triagulo é escaleno')


n1 = float(input('Digite um numero '))
n2 = float(input('Digite outro numero '))

operacao = input('---Escolha a operação desejada---\nSoma(+)\nMultiplicação(*)\nSubtração(-)\nDivisão(/)\n')
conta = 0.0

if operacao == '+':
    conta = n1 + n2
    print('Resultado = {}'.format(conta))
elif operacao == '-':
    conta = n1 - n2
    print('Resultado = {}'.format(conta))
elif operacao == '*':
    conta = n1 * n2
    print('Resultado = {}'.format(conta))
elif operacao == '/':
    conta = n1 / n2
    print('Resultado = {}'.format(conta))
else:
    print('Digite uma operação valida')

kwh = float(input('Digite o consumo de energia '))
instalacao = input('Digite o seu tipo de instalação: \n(r)Residencias\n(i)Industrias\n(c)Comercios\n')
res = 0.0

if instalacao == 'r':    
    if kwh <= 500:
        res = kwh*0.4
        print(res)
    elif kwh > 501:
        res = kwh*0.65
        print(res)          
elif instalacao == 'c':    
    if kwh <= 1000:
        res = kwh*0,55
        print(res)
    elif kwh > 1001:
        res = kwh*0.6        
elif instalacao == 'i':    
    if kwh <= 5000:
        res = kwh*0.55
        print(res)
    elif kwh > 5000:
        res = kwh*0.6
        print(res)
else:
    print('Istalação inexistente')