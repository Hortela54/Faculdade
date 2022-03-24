def dimensoesObjeto():  
    while True:
        try:
            objAltura = int(input('Digite a altura do objeto(cm) '))
            objComprimento = int(input('Digite o comprimento do objeto(cm) '))
            objLargura = int(input('Digite a largura do objeto(cm) '))
        except ValueError:
            print('Você digitou um valor não numerico, digite novamente ')
        else:
            volume = objAltura*objComprimento*objLargura #calculo de volume  
            valor = 0
            if volume < 1000:
                valor = 10
            elif volume >= 1000 and volume < 10000:
                valor = 20
            elif volume >= 10000 and volume < 30000:
                valor = 30
            elif volume >= 30000 and volume < 100000:
                valor = 50
            elif volume >= 100000:
                valor = 'Não aceito'
                continue
            break
    return valor

def pesoObjeto():
    while True:
        try:
            pesoObjeto = int(input('Digite o peso do objeto(kg) '))
        except ValueError:
            print('Erro, valor digitado é invalido')
        else:
            if pesoObjeto < 0.1:
                peso = 1
            elif pesoObjeto >= 0.1 and pesoObjeto < 1:
                peso = 1.5
            elif pesoObjeto >= 1 and pesoObjeto < 10:
                peso = 2
            elif pesoObjeto >= 10 and pesoObjeto < 30:
                peso = 3   
            elif pesoObjeto > 30:
                peso = 'Não aceito'
                continue
            break
    return peso

def rotaObjeto():
    print('+--------------------------------------+')
    print('|RS - De Rio de Janeiro até São Paulo  |')
    print('| SR - De São Paulo até Rio de Janeiro |')    
    print('| BR - De Brasília até Rio de Janeiro  |') 
    print('|   RB - Rio de Janeiro até Brasília   |') 
    print('|    SB - De São Paulo até Brasília    |')  
    print('+--------------------------------------+') 
    rotaObjeto = input('Digite a sigla da rota desejada: ')
    if rotaObjeto == 'RS' or rotaObjeto == 'rs':
        rota = 1
        return rota
    elif rotaObjeto == 'SR' or rotaObjeto == 'sr':
        rota = 1
        return rota
    elif rotaObjeto == 'BS' or rotaObjeto == 'bs':
        rota = 1.2
        return rota
    elif rotaObjeto == 'RB' or rotaObjeto == 'rb':
        rota = 1.5
        return rota
    elif rotaObjeto == 'BR' or rotaObjeto == 'br':
        rota = 1.5
        return rota
    elif rotaObjeto == 'SB' or rotaObjeto == 'sb':
        rota = 1.2
        return rota

def iniciarPrograma():
    print('Bem vindo a Campanhia de Logistica Samuel Nilton da Silva(3892265)')    
    valor = dimensoesObjeto()
    peso = pesoObjeto()
    rota = rotaObjeto()
    total = valor*peso*rota
    print('Total a pagar é R$ {} (dimensões: {} * peso: {} * rota: {})'.format(total,valor,peso,rota))

#Programa Principal
iniciarPrograma() # inicializa o programa 