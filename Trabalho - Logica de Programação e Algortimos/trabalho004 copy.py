from operator import le


pecas = {'cod':[],'nome':[],'fabricante':[], 'valor':[]}
def cadastrarPeca(cod): 
    print('Código da peça: {}'.format(cod))
    nomePeca = input('Digite o nome da peça ') 
    fabricantePeca = input('Digite o nome do fabricante da peça ')
    valorPeca = input('Digite o valor da peça ')   
    pecas['cod'].append(cod)
    pecas['nome'].append(nomePeca)
    pecas['fabricante'].append(fabricantePeca)
    pecas['valor'].append(valorPeca)
    return pecas

def consultarPeca():
    while True:
        print('1 - Consultar todas as peças ')
        print('2 - Consultar peças por Codigo')
        print('3 - Consultar peças por fabricante ')
        print('4 - Retornar ')
        res = int(input('Escolho a opção: '))
        
        if res == 1:
            values = len(pecas['cod']) #Retorna a quantidade de itens dentro, usando o cod como referencia para saber quantas peças existem dentro da lista
            for i in range(0, values): #Varrendo a lista pela quantidade de valores dentro da lista
               print('Codigo {}'.format(pecas['cod'][i]))
               print('Nome {}'.format(pecas['nome'][i]))
               print('Fabricante {}'.format(pecas['fabricante'][i]))
               print('Valor {}'.format(pecas['valor'][i]))
               print('')
        elif res == 2:
            cod = int(input('Digite o codigo para fazer a procura: '))
            values = len(pecas['cod'])
            for i, valor in enumerate(pecas['cod']): #Iterando sobre os valores da lista e seus indices 
                if valor == cod:               
                    print('Codigo {}'.format(pecas['cod'][i]))
                    print('Nome {}'.format(pecas['nome'][i]))
                    print('Fabricante {}'.format(pecas['fabricante'][i]))
                    print('Valor {}'.format(pecas['valor'][i]))
                    print('')
        elif res == 3:
            fabric = input('Digite o fabricante para fazer a procura: ')
            for i, valor in enumerate(pecas['fabricante']):
                if valor == fabric:               
                    print('Codigo {}'.format(pecas['cod'][i]))
                    print('Nome {}'.format(pecas['nome'][i]))
                    print('Fabricante {}'.format(pecas['fabricante'][i]))
                    print('Valor {}'.format(pecas['valor'][i]))
                    print('')
            
        elif res == 4:
            break
        
def removerPeca():
    cod = int(input('Digite o codigo para fazer a procura: '))
    values = len(pecas['cod'])
    for i, valor in enumerate(pecas['cod']): #Iterando sobre os valores da lista e seus indices 
        if valor == cod:               
            print('Codigo {}'.format(pecas['cod'][i]))
            print('Nome {}'.format(pecas['nome'][i]))
            print('Fabricante {}'.format(pecas['fabricante'][i]))
            print('Valor {}'.format(pecas['valor'][i]))
            print('')


def menuPrincipal():
    print('Bem vindo ao Controle de Estoque de Bike Shop do Samuel Nilton da Silva(3892265)')
    codigo = 0 
    while True:
        print('1 - Cadastrar peças ')
        print('2 - Consultar peças ')
        print('3 - Remover peças ')
        print('4 - Sair ')
        res = int(input('Escolho a opção: '))

        if res == 1:
            codigo += 1
            print(cadastrarPeca(codigo))
        elif res == 2:
            consultarPeca()
        elif res == 3:
            print('3')
        elif res == 4:
            break
    
def iniciar(): 
    menuPrincipal()

iniciar()