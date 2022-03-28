def cadastrarPeca(cod):
    while True:
        pecas = {'cod':[cod],'nome':[],'fabricante':[], 'valor':[]}
        nomePeca = input('Digite o nome da peça ') 
        fabricantePeca = input('Digite o nome do fabricante da peça ')
        valorPeca = float(input('Digite o valor da peça '))
        pecas['nome'].append(nomePeca)
        pecas['fabricante'].append(fabricantePeca)
        pecas['valor'].append(valorPeca)
        pecas.clear
        break
              
        

#def consultarPeca():

#def consultarPeca():

#def removerPeca():


cadastrarPeca(1)