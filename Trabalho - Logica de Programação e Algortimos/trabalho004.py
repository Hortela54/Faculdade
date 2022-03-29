def cadastrarPeca(cod): 
    print('Código da peça: {}'.format(cod))
    pecas = {'cod':[cod],'nome':[],'fabricante':[], 'valor':[]}
    while True:
        nomePeca = input('Digite o nome da peça ') 
        fabricantePeca = input('Digite o nome do fabricante da peça ')
        valorPeca = int(input('Digite o valor da peça '))
        pecas['nome'].append(nomePeca)
        pecas['fabricante'].append(fabricantePeca)
        pecas['valor'].append(valorPeca)
        return pecas
        break

def consultarPeca():
    while True:
        print('1 - Consultar todas as peças ')
        print('2 - Consultar peças por Codigo')
        print('3 - Consultar peças por fabricante ')
        print('4 - Retornar ')
        res = int(input('Escolho a opção: '))
        
        if res == 1:
            print('Todas')
            break
        elif res == 2:
            print('Código')
            break
        elif res == 3:
            print('Fabricante')
        elif res == 4:
            break
        

#def removerPeca()

def menuPrincipal():
    print('Bem vindo ao Controle de Estoque de Bike Shop do Samuel Nilton da Silva(3892265)')
    codigo = 0 
    pecas = []
    while True:
        print('1 - Cadastrar peças ')
        print('2 - Consultar peças ')
        print('3 - Remover peças ')
        print('4 - Sair ')
        res = int(input('Escolho a opção: '))

        if res == 1:
            codigo += 1
            pecas.append(cadastrarPeca(codigo))
            print(pecas)
        elif res == 2:
            consultarPeca()
        elif res == 3:
            print('3')
        elif res == 4:
            break
    
def iniciar(): 
    menuPrincipal()

iniciar()