pecas = {'nome':[],'fabricante':[], 'valor':[]}

for i in range(3):
    nomePeca = input('Digite o nome da peça ') 
    fabricantePeca = input('Digite o nome do fabricante da peça ')
    valorPeca = int(input('Digite o valor da peça '))

    pecas['nome'].append(nomePeca)
    pecas['fabricante'].append(fabricantePeca)
    pecas['valor'].append(valorPeca)

print(pecas)