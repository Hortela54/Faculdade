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

cadastrarPeca(1)
teste = cadastrarPeca(2)
print(teste)