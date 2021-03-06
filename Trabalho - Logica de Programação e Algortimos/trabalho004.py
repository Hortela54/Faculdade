pecas = {'cod':[],'nome':[],'fabricante':[], 'valor':[]} #Criando o dicionario e listas com escopo global para savar os cadastros
def cadastrarPeca(cod): #Função para cadastrar os itens 
    print('Código da peça: {}'.format(cod)) #Printa o numero exclusivo de cada item
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
            for i, valor in enumerate(pecas['cod']): #Iterando sobre os valores da lista e seus indices, se orientando pela chave 'cod'
                if valor == cod: # Se o valor do codigo existente for o mesmo que o valor que o usuario digitou                
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
    cod3892265 = int(input('Digite o codigo da peça para fazer a remoção: '))
    values = len(pecas['cod'])
    for i, valor in enumerate(pecas['cod']): #Iterando sobre os valores da lista e seus indices 
        if valor == cod3892265:               
            del(pecas['cod'][i]) #Deletar os registro sendo orientado pelas chaves
            del(pecas['nome'][i])
            del(pecas['fabricante'][i])
            del(pecas['valor'][i])

def menuPrincipal():
    print('Bem vindo ao Controle de Estoque de Bike Shop do Samuel Nilton da Silva(3892265)') #Apresentação com minha RU: 3892265
    codigo = 0 
    while True:
        print('1 - Cadastrar peças ')
        print('2 - Consultar peças ')
        print('3 - Remover peças ')
        print('4 - Sair ')
        res = int(input('Escolho a opção: '))

        if res == 1:
            codigo += 1 #Código exclusivo de cada item 
            cadastrarPeca(codigo) #Inicia a função usando o contador como paramentro
        elif res == 2:
            consultarPeca() #Entra no menu de consulta 
        elif res == 3:
            removerPeca()
        elif res == 4: 
            break #Sair do programa

menuPrincipal()