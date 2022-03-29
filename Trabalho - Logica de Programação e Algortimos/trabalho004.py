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
            for e in pecas:
                for a,b,c,d in e.items():
                    print(a,b,c,d)
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